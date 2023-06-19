from django import forms
from .models import ClientProfile


class ProfileForm(forms.Form):
    firstname = forms.CharField(max_length=32, label='Имя')
    lastname = forms.CharField(max_length=32, label='Фамилия')
    phone = forms.CharField(max_length=32, label='Телефон')
    email = forms.CharField(max_length=32, label='Электронная почта')
    address = forms.CharField(max_length=64, label='Адрес', required=False)
    birth_date = forms.DateField(required=False)

    def clean(self):
        self.cleaned_data = super().clean()
        image = self.cleaned_data.get('image')
        if not image:
            self.cleaned_data['image'] = 'uploads/profile_pics/default/client_avatar.png}'

    def signup(self, request, user):
        user.save()
        profile = ClientProfile()
        profile.user = user
        profile.firstname = self.cleaned_data['firstname']
        profile.lastname = self.cleaned_data['lastname']
        profile.phone = self.cleaned_data['phone']
        profile.email = self.cleaned_data['email']
        profile.address = self.cleaned_data['address']
        profile.birth_date = self.cleaned_data['birth_date']
        profile.image = self.cleaned_data['image']
        profile.save()
