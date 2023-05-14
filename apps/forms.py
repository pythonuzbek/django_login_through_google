from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, PasswordInput, ModelForm
from django.shortcuts import get_object_or_404

from apps.models import User


class RegisterForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and self._meta.model.objects.filter(email__iexact=email).exists():
            self._update_errors(
                ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password do not match")
        password_validation.validate_password(password)
        return make_password(password)



class LoginForm(Form):
    def clean_password(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            raise ValidationError("Password or Username Do Not Match")
        return password