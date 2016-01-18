#Django Email Sender
Sends emails in Django as part of Google Code-in 2015.

##Instructions
1. Install Django: `pip install django` (assuming you have Python with pip installed already) 
2. Clone the repository: `git clone https://github.com/codethejason/email-sender.git`
3. Create Migrations:  `python manage.py makemigrations; python manage.py migrate; python manage.py runserver`
4. Modify the end of *email_sender/settings.py* to match with your Gmail credentials.  
5. Run the server locally: `python manage.py runserver`

##Helpful Resources
[https://docs.djangoproject.com/en/1.9/intro/tutorial01/](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)  
[https://docs.djangoproject.com/en/1.9/topics/email/](https://docs.djangoproject.com/en/1.9/topics/email/)  
