from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='home.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='about.html')

