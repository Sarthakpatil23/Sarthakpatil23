from django import forms
from .models import UploadedFile, PrintingShop, College

class CollegeForm(forms.Form):
    college = forms.ModelChoiceField(queryset=College.objects.all(), empty_label="Select your college")

class PrintingShopForm(forms.Form):
    printing_shop = forms.ModelChoiceField(queryset=PrintingShop.objects.none(), empty_label="Select your printing shop")

    def __init__(self, *args, **kwargs):
        college_id = kwargs.pop('college_id', None)
        super(PrintingShopForm, self).__init__(*args, **kwargs)
        if college_id:
            self.fields['printing_shop'].queryset = PrintingShop.objects.filter(college_id=college_id)

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file', 'color_option', 'print_option', 'additional_instructions', 'time_limit']