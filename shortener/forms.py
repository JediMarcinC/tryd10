from django import forms

from .validators import validate_dot_com, validate_url

class SubmitURLForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

    # def clean(self): # validate form
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     url = cleaned_data['url']
    #     print('url>', url)
    # #
    # def clean_url(self): # validate directly field
    #     url = self.cleaned_data['url']
    #
    #     # print ('from clean_url:', url)
    #     # url_validator = URLValidator()
    #     # try:
    #     #     url_validator(url)
    #     # except:
    #     #     raise forms.ValidationError('Invalid URL!')
    #     return url  # MUST return value to be passed to clean() and views !!!
