from django import forms

class Todolist(forms.Form):
    task = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control" ,'id': "exampleFormControlInput1"}),max_length=80)
    task_priority = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control" ,'id': "exampleFormControlInput1"}),min_value=1,max_value=4)
    

