from django import forms
from django.core.exceptions import ValidationError
from posts.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
 
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана" 

    class Meta:
        model = Musician
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title  
    # title = forms.CharField(max_length = 255, label = 'Заголовок', widget = forms.TextInput(attrs = {'class': 'form-input'}))
    # slug = forms.SlugField(max_length = 255, label = 'URL')
    # content = forms.CharField(widget = forms.Textarea(attrs={'cols': 60, 'rows': 10}), label = 'Текст статьи')
    # is_published = forms.BooleanField(label = 'Опубликовано', required = False, initial = True)
    # cat = forms.ModelChoiceField(queryset = Category.objects.all(), label = 'Жанр', empty_label = 'Категория не выбрана')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput (attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput (attrs={'class': 'form-input'})) 
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput (attrs={'class': 'form-input'})) 
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput (attrs={'class': 'form-input'}))
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput (attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput (attrs={'class': 'form-input'})) 

class ContactForm(forms.Form):

    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

class AddCommForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'].empty_label = "Пост не выбран" 

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
   