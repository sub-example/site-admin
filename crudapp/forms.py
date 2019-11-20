from django import forms
from .models import InfoModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class TestForm(forms.Form):
    text = forms.CharField(label='文字列')
    num = forms.IntegerField(label='数値')
    email = forms.EmailField(label='メール')
    #date = forms.DateField(auto_now=False,label='日付')

#InfoModelFormに補足情報としてMeta情報を加えている。
#ModelFormクラスを継承し、fieldsを定義する。
class InfoModelFormAdd(forms.ModelForm):
    class Meta:
        model = InfoModelForm
        fields = ['name','mail','gender','department','year','created_at']
        
class SignUpForm(forms.Form):
    #フィールド三つ。名前とパスワード、
    username = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
    #?
    #widgetでキー入力が画面に表示されないようにする。
    retype_password = forms.CharField(widget=forms.PasswordInput)
    #ユーザーネームがすでにある場合、レイズする。
    def clearn_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username
    #パスワードのバリデーション
    def clearn_enter_password(self):
        password= self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password
    #どちらかが空か、２つ違うとき
    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_pasword', 'This does not match with the above.')
            #retypeのフィールドにエラーを紐づけている。
            
    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        new_user = User.objects.create_user(username = username)
        new_user.set_password(password)
        new_user.save()
        
class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwards):
        super().__init__(*args,**kwards)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label