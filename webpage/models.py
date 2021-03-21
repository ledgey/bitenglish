from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    agree_marketing = models.BooleanField(default=False)
    message = models.CharField(max_length=500, null=True)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message','agree_marketing')
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        labels = {
            'name': _('Name'),
            'agree_marketing': _('I consent to be contacted'),
            'message': _('Message'),
        }

        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
