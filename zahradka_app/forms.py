from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from zahradka_app.models import Garden, Plant, Membership, UserMembership, Subscription


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['name', 'description', 'address', 'plant']

    plant = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Plant.objects.all())

    def save(self, user):
        garden = super().save(commit=False)
        garden.user = user
        garden.save()
        garden.plant.add(*self.cleaned_data.get('plant'))

    def clean_plant(self):
        value = self.cleaned_data['plant']
        if len(value) > 3:
            raise forms.ValidationError("Pokud nejste naším členem, je možné vybrat max. 3 rostliny. ")
        return value


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class SignUpForm(UserCreationForm):
    try:
        free_membership = Membership.objects.get(membership_type=Membership.FREE)
    except Membership.DoesNotExist:
        pass


    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.save()
        return user
