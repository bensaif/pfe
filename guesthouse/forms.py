from django import forms
from django.forms import ModelForm
from .models import Hebergement, Reshebergement,Ressalle, Salle


class ReshebergementForm(forms.ModelForm):
    class Meta:
        model = Reshebergement
        fields ="__all__"  
        widgets = {
            'Courrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'Etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'Demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'Capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'DateEntree': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ChambreDisponible': forms.TextInput(attrs={'class': 'form-control'}),
            'PriseEnCharge': forms.TextInput(attrs={'class': 'form-control'}),
            'Moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'Statue': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.TextInput(attrs={'class': 'form-control'}),
        }      

class RessalleForm(forms.ModelForm):
    class Meta:
        model = Ressalle
        fields =['etablissement', 'demandeur', 'dateEntrée', 'dateSortie', 'nomSalleDisponible', 'nombrePersonne', 'typeEvenement', 'dejeuner', 'pauseCafe', 'nombrecourrier', 'moyen', 'statue', 'commentaire']
        widgets = {
            'dateEntrée': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'nomSalleDisponible': forms.TextInput(attrs={'class': 'form-control'}),
            'nombrePersonne': forms.NumberInput(attrs={'class': 'form-control'}),
            'typeEvenement': forms.TextInput(attrs={'class': 'form-control'}),
            'dejeuner': forms.NumberInput(attrs={'class': 'form-control'}),
            'pauseCafe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombrecourrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'statue': forms.TextInput(attrs={'class': 'form-control'}),
            'commentaire': forms.TextInput(attrs={'class': 'form-control'}),
        }                                          

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