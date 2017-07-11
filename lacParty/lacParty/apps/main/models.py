# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Photography(models.Model):

    image = models.ImageField(upload_to="Gallery")   #upload_to significa que va a esa carpeta


    create_at = models.DateTimeField(auto_now_add=True) # Fecha de Cuando se creo
    updated_at = models.DateTimeField(auto_now=True) # Fecha de cuando se modifico
