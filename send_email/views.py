from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def done(request):
    email = request.POST.get('email', '')
    content = "Hello there, the email came through! Be sure to checkout FOSSASIA!"
    send_mail('It Works!', content, 'from@example.com',
    [email], fail_silently=False)
    return render(request, 'done.html')
