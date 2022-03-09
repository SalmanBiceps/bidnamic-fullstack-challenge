from django import forms
from datetime import datetime, date
from django.core.exceptions import ValidationError

from .models import Bidding


class BiddingForm(forms.ModelForm):
    # dob = forms.DateField()

    BIDDING_OPTIONS = [
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW'),
    ]
    # bidding = forms.ChoiceField(choices=BIDDING_OPTIONS)

    def validate_digits_letters(self,word, field_title):
        for char in word:
            if char.isdigit() or (char.isdigit() and char.isalpha()):
                raise forms.ValidationError(
                    "Please enter a correct " + field_title)
    def clean_first_name(self):
        field_title = "first_name"
        data = self.cleaned_data[field_title]
        self.validate_digits_letters(data, field_title)
        return data
    def clean_surname(self):
        field_title = "surname"
        data = self.cleaned_data[field_title]
        self.validate_digits_letters(data, field_title)
        return data
    def clean_city(self):
        field_title = "city"
        data = self.cleaned_data[field_title]
        self.validate_digits_letters(data, field_title)
        return data
    def clean_state(self):
        field_title = "state"
        data = self.cleaned_data[field_title]
        self.validate_digits_letters(data, field_title)
        return data
    def clean_telephone(self):
        field_title = "telephone"
        data = self.cleaned_data[field_title]
        for char in data:
            if not char.isdigit():
                raise forms.ValidationError(
                    "Please enter a correct " + field_title)
        return data
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        print("hiiiiiiiii", self.cleaned_data['dob'])
        age = (date.today() - dob).days/365
        if age < 18:
            raise ValidationError(
                'Must be at least 18 years old to submit a bidding')
        elif age > 100:
            raise ValidationError(
                'Please enter a correct age to bidding')
        return dob

    class Meta:
        model = Bidding
        fields = ['title', 'first_name', 'surname', 'dob', 'company_name',
                  'address_1', 'address_2', 'city', 'state', 'postcode', 'telephone', 'bidding', 'google_ads_account_id']
        widgets = {
            'bidding': forms.Select(attrs={'class': 'form-select text-center'}),
        }
        
