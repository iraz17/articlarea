from django import forms

class CartForm(forms.Form):
    quantity = forms.IntegerField(label='Quantité', min_value=1)
    # Ajoutez d'autres champs si nécessaire