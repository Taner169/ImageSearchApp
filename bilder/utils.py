import openai
from django.conf import settings
from google.cloud import storage
import datetime

openai.api_key = settings.OPENAI_API_KEY

def generate_signed_url(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(expiration=datetime.timedelta(minutes=60), method='GET')
    return url

def generate_description(image_url):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f" Your prompt here {image_url}",
            max_tokens=150,
            temperature=0.5,
            top_p=1.0,
            api_key=settings.OPENAI_API_KEY
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Failed to generate description: {str(e)}"
