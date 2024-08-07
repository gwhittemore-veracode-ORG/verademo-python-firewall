# homeController.py deals with the default website redirection.

from django.shortcuts import redirect
from .userController import login
import urllib

# redirects user to feed if they are already logged in, otherwise sends to login
def home(request):
    # Equivalent of HomeController.java
    if request.session.get('username'):
        # START BAD CODE
        try:
            host_ip = request.META['HTTP_HOST'].split(':')[0]
            redir = urllib.request.Request('http://' + host_ip + ':' + request.META['SERVER_PORT'] + '/feed')
            urllib.request.urlopen(redir)
        # END BAD CODE
        except: 
            # GOOD CODE:
            return redirect('feed')
        
       
    
    return login(request)

