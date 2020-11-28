from django.shortcuts import render
from django.http import JsonResponse

from django.conf import settings


def get_version(request):
    ''' This view returns version of the project. It returns json response in format {'version': 'v1' }'''
    return JsonResponse({'version':settings.VERSION})
