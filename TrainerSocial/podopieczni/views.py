from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from podopieczni.models import Podopieczny, PodopiecznyMember
from django.contrib import messages
from django.db import IntegrityError
from . import models
from django.core.files import File
from django.core.urlresolvers import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from . import views

def wiadomosc():
    send_mail(
    'Nowy plan treningu',
    'Twój nowy plan treningowy',
    'jntestowymail@gmail.com',
    ['jntestowymail@gmail.com'],
    fail_silently=False,
    )


class CreatePodopieczny(LoginRequiredMixin, generic.CreateView):
    fields = ["imię_i_nazwisko","email","płeć","wzrost","waga","opis","cel","rodzaj_treningu","plan"]
    model = Podopieczny
    

class SinglePodopieczny(generic.DetailView):
    model = Podopieczny

class ListPodopieczni(generic.ListView):
    model = Podopieczny


class JoinPodopieczny(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('podopieczni:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        podopieczny = get_object_or_404(Podopieczny,slug=self.kwargs.get('slug'))
        try:
            PodopiecznyMember.objects.create(user=self.request.user,podopieczny=podopieczny)
        except IntegrityError:
            messages.warning(self.request,'Masz już dostęp do tego profilu!')
        else:
            messages.success(self.request, 'Dostałeś dostęp do tego profilu')

        return super().get(request,*args,**kwargs)


class LeavePodopieczny(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('podopieczni:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = models.PodopiecznyMember.objects.filter(
                user=self.request.user,
                podopieczny__slug=self.kwargs.get('slug')
            ).get()
        except models.PodopiecznyMember.DoesNotExist:
            messages.warning(self.request,'Nie masz dostępu do tego profilu!')
        else:
            membership.delete()
            messages.success(self.request, 'Opuściłeś profil podopiecznego!')
        return super().get(request,*args,*kwargs)
