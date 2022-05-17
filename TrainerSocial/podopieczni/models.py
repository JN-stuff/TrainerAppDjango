from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files import File
#PODOPIECZNI MODELS.PY
# Create your models here.
from django.core.mail import send_mail
from django.core import mail
from django.core.mail import EmailMessage
import os
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()



class Podopieczny(models.Model):

    MALE = 'Mężczyzna'
    FEMALE = 'Kobieta'

    sex_choices = (
        (MALE,'Mężczyzna'),
        (FEMALE,'Kobieta'),
    )

    imię_i_nazwisko = models.CharField(max_length=155,unique=False)
    płeć = models.CharField(choices=sex_choices,max_length=64,default='')
    wzrost = models.CharField(max_length=64,default='')
    waga = models.CharField(max_length=64,default='')
    cel = models.CharField(max_length=64,default='')
    rodzaj_treningu = models.TextField(default='', blank=False)
    slug = models.SlugField(allow_unicode=True, unique=True)
    opis = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User, through="PodopiecznyMember")
    plan = models.FileField(upload_to='plany/')
    email = models.EmailField(max_length=64,unique=True,blank=False,default='')

    def __str__(self):
        return self.imię_i_nazwisko

    def save(self,*args,**kwargs):
        self.slug = slugify(self.imię_i_nazwisko)
        self.description_html = misaka.html(self.opis)
        super().save(*args,**kwargs)
        






    def get_absolute_url(self):
        return reverse('podopieczni:single',kwargs={"slug":self.slug})

    class Meta:
        ordering = ['imię_i_nazwisko']

class PodopiecznyMember(models.Model):
    podopieczny = models.ForeignKey(Podopieczny, related_name='membership')
    user = models.ForeignKey(User,related_name='user_podpieczni')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('podopieczny','user')
