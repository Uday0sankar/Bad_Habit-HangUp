from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'whatsapp.html')

def WhatsappMsg(ph,message):
    import time
    import webbrowser as web
    import pyautogui as pg

    Phone = '+91'+ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+message)
    time.sleep(30)
    pg.press('enter')


def SendData(request):
    if request.method=='POST':
        ph = request.POST['Phone']
        message = request.POST['Message']
        WhatsappMsg(ph,message)
        msg = 'Message is sent'
        return render(request,'whatsapp.html',{'msg':msg})
    else:
        
        return HttpResponse('404 fot found')