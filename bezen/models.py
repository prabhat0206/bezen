from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def resize_image(image):
    size = 140
    rimage = Image.open(image)
    rimage.thumbnail((220, 200), Image.ADAPTIVE)
    rimage = crop_center(rimage, size, size)
    rimage.save(image)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    species = models.CharField(max_length=255)
    weight = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)
        self.image = resize_image(self.image.path)