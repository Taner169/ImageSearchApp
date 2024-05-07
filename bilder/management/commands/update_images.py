from django.core.management.base import BaseCommand
from google.cloud import storage
from django.conf import settings
from bilder.models import Bild
from bilder.utils import generate_description

class Command(BaseCommand):
    help = 'Updates image descriptions from Google Cloud Storage'

    def handle(self, *args, **options):
        storage_client = storage.Client()
        bucket = storage_client.bucket(settings.GCS_BUCKET_NAME)
        blobs = bucket.list_blobs()

        for blob in blobs:
            image_url = blob.public_url
            existing_image = Bild.objects.filter(name=blob.name).first()
            if not existing_image:
                description = generate_description(image_url)
                new_image = Bild(name=blob.name, image_url=image_url, description=description)
                new_image.save()
            else:
                # Update description if necessary
                existing_image.description = generate_description(image_url)
                existing_image.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated image descriptions.'))
