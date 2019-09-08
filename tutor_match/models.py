from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
class Tutor(auth_models.User):
    fullName = models.CharField('First Last', max_length=64)
    priceID = models.DecimalField('Price ID', max_digits=5, decimal_places=2)
    classID = models.CharField('Class ID', max_length=128)
    contact = models.TextField('Contact', max_length=256)
    rating = models.DecimalField('Rating', max_digits=2, decimal_places=1)
    template = models.CharField('Template', max_length=256, blank = True)
    # add = Tutor(username = "0", password = "", email = "", fullName = "", priceID = 0, classID = "", contact =" ", rating = 0)

    # In the future add arrays to price and classes after switching form the test sql environment to a post
        #  for i in Tutor.objects.all():    
        # if (i.username == "0"):
        #     continue
        # else:
        #     i.delete()
