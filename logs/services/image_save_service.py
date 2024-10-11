import base64
import os
from django.core.files.base import ContentFile
from django.utils import timezone


def save_screenshot(data_url):
    format, imgstr = data_url.split(';base64,')
    ext = format.split('/')[-1]
    image_data = ContentFile(base64.b64decode(imgstr), name=f"screenshot_{timezone.now()}.{ext}")

    path = os.path.join('media', 'screenshots', image_data.name)
    with open(path, 'wb') as f:
        f.write(image_data.read())
    return path
