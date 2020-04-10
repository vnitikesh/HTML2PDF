from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

# Create your views here.

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = render_to_pdf('invoice.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')