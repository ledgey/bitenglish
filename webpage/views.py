from django.shortcuts import render
from django.views import View

# add to the top
from .models import ContactForm, Contact

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

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

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'home.html', {'form': form_class})

# class Home(View):
#     def get(self, request, *args, **kwargs):
#         form_class = ContactForm
#         return render(request, 'home.html', {'form': form_class})




class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='about.html')


