from django import forms

class OrderForm(forms.Form):
    cName = forms.CharField(label='訂購者',max_length=20, initial = '', widget=forms.TextInput(
        attrs={
           'class': 'form-control',
        }
    ))
    cSpot = forms.CharField(max_length=20, initial='自取')
    cPhone = forms.CharField(max_length=10, initial='', widget=forms.TextInput(
        attrs={
           'class': 'form-control',
        }
    ))
    cDate = forms.DateField(widget=forms.TextInput(
        attrs={
           'class': 'form-control',
           'id': 'datepicker',
           'placeholder': '請選擇日期',
        }
    ))

    c1T100 = forms.IntegerField(initial='0', required = False)
    c1T100_slice = forms.CharField(max_length=10, initial='不切')
    c1T100_thickless = forms.CharField(max_length=10, initial = '')


    c1T120 = forms.IntegerField(initial='0', required = False)
    c1T120_slice = forms.CharField(max_length=10, initial='不切')
    c1T120_thickless = forms.CharField(max_length=10, initial = '')

    c1T130 = forms.IntegerField(initial='0', required = False)
    c1T130_slice = forms.CharField(max_length=10, initial='不切')
    c1T130_thickless = forms.CharField(max_length=10, initial = '')

    c1T140 = forms.IntegerField(initial='0', required = False)
    c1T140_slice = forms.CharField(max_length=10, initial='不切')
    c1T140_thickless = forms.CharField(max_length=10, initial = '')

    c2M50 = forms.IntegerField(initial='0', required = False)
    c2M50_slice = forms.CharField(max_length=10, initial='不切')
