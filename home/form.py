# coding=utf-8
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"Old password",
        error_messages={'required': u'Please input your old password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"Old password",
                'style': u"",
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"New password",
        error_messages={'required': u'Please input your new password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"New password",
                'style': u"",

            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"Repeat password",
        error_messages={'required': u'Please input your new password again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"Confirm new password",
                'style': u"",

            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data