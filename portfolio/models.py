from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    # telling django where to save uploaded images.
    # Note that we don't have to manually create the folders stated in the upload_to parameter above.
    # But we need to define MEDIA_ROOT in settings.py.    
    # Note that to use ImageFieald (or to upload images), you need to 
    # install pillow. pip install pillow
    # To be able to open our image from the site, we also need to add MEDIA_URL to settings.py
    # ans also add static to urlpatterns in the project's urls.py
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


