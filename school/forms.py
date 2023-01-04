from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields=('surname','First_Name','Other_Name','Date_of_Birth','postal_address','Residential_Address','Latest_school_addresss',
        'Latest_class_Attended','Home_telephone_number','name_of_father','Occupation_of_Father','Contact_address_of_Father',
        'tel_No_of_Father','name_of_mother','Occupation_of_mother','Contact_address_of_mother','tel_No_of_mother','who_to_call_in_case_of_emergency',
        'any_allergy_or_physical_deafect','picture')

        widgets={
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'First_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Other_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_Birth':forms.DateInput(attrs={'class':'form-control'}),
            'postal_address':forms.TextInput(attrs={'class':'form-control'}),
            'Residential_Address':forms.TextInput(attrs={'class':'form-control'}),
            'Latest_school_addresss':forms.TextInput(attrs={'class':'form-control'}),
            'Latest_class_Attended':forms.Select(attrs={'class':'form-control'}),
            'Home_telephone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'name_of_father':forms.TextInput(attrs={'class':'form-control'}),
            'Occupation_of_Father':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_address_of_Father':forms.TextInput(attrs={'class':'form-control'}),
            'tel_No_of_Father':forms.NumberInput(attrs={'class':'form-control'}),
            'name_of_mother':forms.TextInput(attrs={'class':'form-control'}),
            'Occupation_of_mother':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_address_of_mother':forms.TextInput(attrs={'class':'form-control'}),
            'tel_No_of_mother':forms.NumberInput(attrs={'class':'form-control'}),
            'who_to_call_in_case_of_emergency':forms.TextInput(attrs={'class':'form-control'}),
            'any_allergy_or_physical_deafect':forms.Textarea(attrs={'class':'form-control'}),


        }