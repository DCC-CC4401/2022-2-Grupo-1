from django import forms


class NewRecipeForm(forms.Form):
    name = forms.CharField(label="Título", max_length=100)
    image = forms.FileField(required=False)
    ingredients = forms.CharField(label="Ingredientes", max_length=5000, widget=forms.Textarea)
    instructions = forms.CharField(label="Instrucciones", max_length=5000, widget=forms.Textarea)
