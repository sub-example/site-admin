from django import forms
from .models import InfoModelForm

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