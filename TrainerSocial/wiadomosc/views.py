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
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
# Create your views here.
class wiadomosc(LoginRequiredMixin, generic.CreateView):
    fields = ["imię_i_nazwisko","email","tytuł_wiadomości","treść_wiadomości"]
