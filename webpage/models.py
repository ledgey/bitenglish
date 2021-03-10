from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    business_name = models.CharField(max_length=100)
    email = models.EmailField()
    business_type = models.CharField(max_length=100, choices=TITLE_CHOICES)
    employee_num = models.CharField(max_length=20, choices=TITLE_CHOICES)
    agree_marketing = models.BooleanField(default=False)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'business_name', 'business_type', 'employee_num', 'agree_marketing')
        labels = {
            'name': _('Name'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


