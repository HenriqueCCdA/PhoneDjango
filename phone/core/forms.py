from django import forms

from phone.core.models import Phone


class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = ('number',)
