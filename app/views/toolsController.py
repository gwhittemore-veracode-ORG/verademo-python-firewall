# toolsController.py deals with the 'Tools' page and calls the tool functions used in the page
import logging
import subprocess


from django.shortcuts import render
from app.fortune.fortuneData import FortuneData
from app.fortune.fortuneData import RiddleData

logger = logging.getLogger("VeraDemo:toolsController")

# Redirects request based on type
def tools(request):
    if(request.method == "GET"):
        return showTools(request)
    elif(request.method == "POST"):
        return processTools(request)

# Loads the tool webpage    
def showTools(request):
    request.host = ""
    return render(request, 'app/tools.html', {})

# Performs the actions on the tool page, updating output accordingly
def processTools(request):
    host = request.POST.get('host')
    fortunefile = request.POST.get('fortunefile')
    request.file = fortune() if fortunefile else ""
    request.host = host
    request.ping = ping(host) if host else ""
    
    

    return render(request, 'app/tools.html', {"host" : host})

# pings selected host and outputs the result
def ping(host):
    output = ""
    logger.info("Pinging " + host)
    try:
        p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout = p.communicate(timeout=5)
    
        output = stdout.decode() if stdout else ""
        logger.info(output)
        logger.info("Exit Code:", p.returncode)
    except subprocess.TimeoutExpired:
        logger.error("Ping timed out")
        output = "ping: unknown host " + host
    except Exception as e:  
        logger.error("Error", e)
        output = "ping: unknown host " + host

    return output


# Produces a fortune based on the submitted selection
def fortune():
    logger.info("Entering fortune")

    fortune = FortuneData()
    print(fortune.next())
     
    return fortune




   