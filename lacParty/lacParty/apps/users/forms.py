from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Usuario'
    }))
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'Contraseña'
    }))

    def clean(self): #con esta funcion envia los json del formulario    "partyluis"
        user_found = User.objects.filter(username = 'partyluis')
         #el filter trae una lista de objectos pero si lo combina con el existi solo retorna un true o false
        if not user_found:
            self.add_error('username','Usuario y/o Contraseña no encontrados') #mandas un mensaje de error a la caja de texto
        else:
            user = User.objects.get(username = 'partyluis') # El Get trae solo un objeto  fiestafiesta
            if not user.check_password(self.cleaned_data['password']):
                self.add_error('password','Contraseña Incorrecta')
