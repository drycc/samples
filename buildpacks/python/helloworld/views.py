import os
import string
import random
import subprocess

from django.http import HttpResponse


def index(request):
    whom = os.getenv('POWERED_BY', 'Drycc')
    release = os.getenv('WORKFLOW_RELEASE', 'unknown')
    container = subprocess.getoutput('hostname').strip()
    return HttpResponse('Powered by {whom}\nRelease {release} on {container}'.format(**locals()))

def letters(request):
    size = int(request.GET.get('size', '128'))
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    print(data)
    return HttpResponse(data)


# Return 200 for kubernetes healthcheck.
def healthz(request):
    return HttpResponse('')
