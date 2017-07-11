# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse 
from apps.main.models import Photography
from django.http import HttpResponse
from django.views.generic.edit import CreateView



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        context['photographys'] = Photography.objects.all()
        return context


def FormView(request):
    return render(request, "upload.html")


def UploadView(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            url = './Gallery/' + str(x.name)
            with open(url, 'wb+') as destination:
                obj = Photography(image=url)
                obj.save()
                print (url)
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return redirect(reverse('main:home'))
