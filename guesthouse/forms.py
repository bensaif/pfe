from django import forms
from django.forms import ModelForm
from .models import Hebergement, Reshebergement,Ressalle, Salle


class ReshebergementForm(forms.ModelForm):
    class Meta:
        model = Reshebergement
        fields = [
            'idhebergement','etablissement', 'Demandeur', 'Courrier', 'DateEntre', 'DateSortie', 
            'Capacite', 'hebergement', 'PriseenCharge', 'Type', 'Moyen', 'Statut'
        ] 
        widgets = {
            'Courrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'Demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'Capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'DateEntre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hebergement': forms.TextInput(attrs={'class': 'form-control'}),
            'PriseenCharge': forms.TextInput(attrs={'class': 'form-control'}),
            'Moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'Statut': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.TextInput(attrs={'class': 'form-control'}),
        }      
        Hebergement = forms.ModelChoiceField(queryset=Hebergement.objects.all(), label="Heberhement")
    
class RessalleForm(forms.ModelForm):
    class Meta:
        model = Ressalle
        fields =['idressalle','etablissement','priseEnCharge', 'demandeur', 'dateEntrée', 'dateSortie', 'Salle', 'nombrePersonne', 'sujet', 'dejeuner', 'pauseCafe', 'courrier', 'moyen', 'statut', 'commentaire']
        widgets = {
            'dateEntrée': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'nombrePersonne': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'dejeuner': forms.Select(choices=Ressalle.DEJEUNER_CHOICES),
            'pauseCafe': forms.Select(choices=Ressalle.PAUSE_CAFE_CHOICES),
            'courrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'priseEnCharge': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.TextInput(attrs={'class': 'form-control'}),
            'commentaire': forms.TextInput(attrs={'class': 'form-control'}),
        }                                          

        salle = forms.ModelChoiceField(queryset=Salle.objects.all(), label="Salle de réunion")
class SalleForm(ModelForm):
    class Meta:
        model=Salle
        fields="__all__"  
        exclude=['idsalle']   

class HebergementForm(ModelForm):
    class Meta:
        model=Hebergement
        fields="__all__"
        exclude=['idchambre']   
        