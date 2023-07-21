from django.shortcuts import render
from .utils import get_website_url

def index(request):
    website_url = None
    if request.method == 'POST':
        site_name = request.POST['site_name']
        website_url = get_website_url(site_name)
    
    return render(request, 'index.html', {'website_url': website_url})
