from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.


def index(request):
    return render(request, 'index.html')

def done(request):
    email = request.POST.get('email', '')
    confirm = request.POST.get('checkbox', '')
    try:
        validate_email(email)
        except ValidationError as e:
        return render(request, 'error.html')
    content = "Hello there, the email came through! Be sure to checkout FOSSASIA!"
    if confirm == 'on':
      send_mail('It Works!', content, 'from@example.com',
      [email], fail_silently=False)
      return render(request, 'done.html')
