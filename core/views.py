from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def main(request):
    """Render HTML to show WebMAP

    :param layername: The webmap name in Geonode.
    :type layername: basestring

    :return: The HTTPResponse
    """

    context = {}
    return render(request, 'django_main.html', context)
