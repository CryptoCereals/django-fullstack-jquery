from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging
logger = logging.getLogger('django_onepage')

@login_required
def index(request):
    """Onepage index rendering"""
    context = {}
    return render(request, "django_main.html", context)