# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse, reverse_lazy
from apps.main.models import Photography
from django.http import HttpResponse
from PIL import Image
from .forms import UploadForm
from django.views.generic.edit import CreateView, FormView



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        context['photographys'] = Photography.objects.all()
        return context

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = reverse_lazy('main:home')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for f in files:
                obj = Photography(image= f)
                obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# def FormView(request):
#     return render(request, "upload.html")
#
#
# def UploadView(request):
#     for count, x in enumerate(request.FILES.getlist("files")):
#         def process(f):
#             url = './Gallery/' + str(x.name)
#             with open(url, 'wb+') as destination:
#                 obj = Photography(image=url)
#                 obj.save()
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#         img = Image.open(x['file'])
#         img.save(x['file'], format='JPEG', quality=70)
#         process(x)
#     return redirect(reverse('main:home'))



    # def UploadView(request):
    #     for count, x in enumerate(request.FILES.getlist("files")):
    #         def process(f):
    #             url = './Gallery/' + str(x.name)
    #             with open(url, 'wb+') as destination:
    #                 obj = Photography(image=url)
    #                 obj.save()
    #                 print (url)
    #                 for chunk in f.chunks():
    #                     destination.write(chunk)
    #         process(x)
    #     return redirect(reverse('main:home'))
