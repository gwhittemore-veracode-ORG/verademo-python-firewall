# homeController.py deals with the default website redirection.

from django.shortcuts import redirect, render
from .userController import login
import urllib

# redirects user to feed if they are already logged in, otherwise sends to login
def home(request):
    # Equivalent of HomeController.java
    if request.session.get('username'):
        # START BAD CODE
        # redir = urllib.request.Request('http://' + request.META['HTTP_HOST'] + '/feed')
        try:
            urllib.request.urlopen('http://' + request.META['HTTP_HOST'] + '/feed', timeout=3)
        except Exception as e:
            return redirect('feed')
        # END BAD CODE
        # GOOD CODE:
        # return redirect('feed')
    
    return login(request)