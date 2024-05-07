from django.core.management.base import BaseCommand
from google.cloud import storage
from django.conf import settings
import openai
from bilder.models import Bild  

class Command(BaseCommand):
    help = 'Updates image descriptions using OpenAI'

    def handle(self, *args, **options):
        self.stdout.write("Updating image descriptions...")
        update_image_descriptions()
        self.stdout.write(self.style.SUCCESS('Successfully updated image descriptions.'))

def update_image_descriptions():
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.GCS_BUCKET_NAME)
    blobs = bucket.list_blobs()

    for blob in blobs:
        image_url = blob.public_url
        existing_image = Bild.objects.filter(name=blob.name).first()

        if not existing_image or existing_image.description == "":
            description = get_image_description(image_url)

            if existing_image:
                existing_image.description = description
                existing_image.save()
            else:
                new_image = Bild(name=blob.name, image_url=image_url, description=description)
                new_image.save()

def get_image_description(image_url):
    """
    Generates a description of an image using OpenAI's API.
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f" Your prompt here {image_url}",
            max_tokens=150,
            temperature=0.5,
            top_p=1.0,
            api_key=settings.OPENAI_API_KEY
        )
        description = response.choices[0].text.strip()
        return description
    except Exception as e:
        print(f"Failed to generate description: {str(e)}")
        return "Description could not be generated."