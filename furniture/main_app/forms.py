from django import forms

from main_app.models import User_table, cart_table
from main_app.models import User


class Usersignupform(forms.ModelForm):
    password=forms.CharField(widget=forms.TextInput(attrs={"type":"password"}))

    def __init(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"]="form-control"
            
    class Meta:
        model = User_table
        fields = [
            "firstname",
            "lastname",
            "email",
            "username",
            "password",
            "Address",
            ]
    


class LoginForm(forms.ModelForm):

    password=forms.CharField(widget=forms.TextInput(attrs={"type":"password"}))
    
    def __init(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"]="form-control"

    class Meta:
        model=User_table
        fields=["username","password"]



class usercart_table(forms.ModelForm):
    def __init(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"]="form-control"

    class Meta:
        model=cart_table
        fields='__all__'


