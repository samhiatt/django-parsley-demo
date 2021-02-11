# Django Parsley Demo Application

This Django app is to demonstrate how to use [django-parsely](https://github.com/agiliq/Django-parsley) 
to replicate Django Form validation on client side.  
Additionally, it shows how to use parsley in combination with 
[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) 
and [bootstrap4](https://getbootstrap.com/docs/4.5).


Original app by Emad Mokhtar. 
See [his blog post](emadmokhtar.com/client-side-validation-for-django-forms.html) 
for more info.

Also thanks to Vitor Freitas' blog post 
[How to Use Django Widget Tweaks](https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html)
for help with using django-widget-tweaks to customize form elements with bootstrap.

# How to Run

1. Install Dependencies `pip install -r requirements.txt`
2. Migrate `python manage.py migrate`
3. Run Dev Sever `python manage.py runserver`
