from django.shortcuts import render
from django.views import View
import json
# add to the top
from .models import ContactForm, Contact


from django.core.mail import EmailMessage
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse

# our view
def home(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'name'
                , '')
            contact_email = request.POST.get(
                'email'
                , '')
            message = request.POST.get('message')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['chris@bit-english.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return HttpResponse(json.dumps({"success":True}), content_type="application/json")


    return render(request, 'home.html', {'form': form_class, 'submission': False})

# class Home(View):
#     def get(self, request, *args, **kwargs):
#         form_class = ContactForm
#         return render(request, 'home.html', {'form': form_class})




class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='about.html')


