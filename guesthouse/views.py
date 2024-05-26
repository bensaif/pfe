
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.utils.translation import gettext_lazy as _
from .forms import *
from django.shortcuts import render
from django.http import JsonResponse 

from django.db import transaction
from django.http import HttpResponse
from .signals import log_reservation_save, log_reservation_delete

def create_reservation(request):
    with transaction.atomic():
        reservation = Reservation.objects.create(
            name=request.POST['name'],
            date=request.POST['date']
        )
        log_reservation_save(Reservation, reservation, created=True, request=request)
    return HttpResponse("Réservation créée")

def update_reservation(request, pk):
    with transaction.atomic():
        reservation = Reservation.objects.get(pk=pk)
        reservation.name = request.POST['name']
        reservation.date = request.POST['date']
        reservation.save()
        log_reservation_save(Reservation, reservation, created=False, request=request)
    return HttpResponse("Réservation mise à jour")

def delete_reservation(request, pk):
    with transaction.atomic():
        reservation = Reservation.objects.get(pk=pk)
        log_reservation_delete(Reservation, reservation, request=request)
        reservation.delete()
    return HttpResponse("Réservation supprimée")


def salle_form_view(request):
    form = RessalleForm()  
    
    if request.method == 'POST':
        form = RessalleForm(request.POST)
        if form.is_valid():
            form.save()
            GuestHouseEvent.objects.create(
                title=form.cleaned_data['etablissement'],
                start_time=form.cleaned_data['dateEntrée'],  # Correct field name
                end_time=form.cleaned_data['dateSortie'] 
            )

            return redirect('RessalleForm')
    
    return render(request, 'salle.html', {'form': form})

def home(request):
    context = {'role': None}
    user = request.user
    if user and user.is_authenticated:
        role = Role.objects.filter(user=user).first()
        context = {'role': role}
    return render(request, 'home.html', context=context)

def reservation(request):
    return render(request, 'reservation.html')

def admin(request):
    return render(request, 'admin.html')

def payement(request):
    return render(request, 'payement.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            return render(request, 'connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('home')


def hebergement_form_view(request):
    form = ReshebergementForm()  
    
    if request.method == 'POST':
        form = ReshebergementForm(request.POST)
        if form.is_valid():
            form.save()
            GuestHouseEvent.objects.create(
                title=form.cleaned_data['nom'],
                start_time=form.cleaned_data['date'],
                end_time=form.cleaned_data['date']
            )
           
            return redirect('ReshebergementForm')
    
    return render(request, 'hebergement.html', {'form': form})



def liste_attributs(request):
    liste_attributs = Ressalle.objects.all()
    return render(request, "liste.html", {'liste_attributs': liste_attributs})
def liste_chambre(request):
    liste_chambre = Reshebergement.objects.all()
    return render(request, "listehebergement.html", {'liste_chambre': liste_chambre})
def update(request):
    obj=Ressalle.objects.get(idressalle=3)
    form = RessalleForm(request.POST or None,instance=obj)  
    messages = ''

    if form.is_valid():
        form.save()
        form = RessalleForm()
        messages = "modification avec succès"
    
    return render(request, 'edit.html', {'form': form, 'message': messages})

def delete_ressalle(request, idressalle):
    # Utiliser get_object_or_404 pour obtenir l'objet ou renvoyer une page 404 si l'objet n'existe pas
    obj = get_object_or_404(Ressalle, idressalle=idressalle)
    
    if request.method == "POST":
        # Supprimer l'objet si la méthode est POST
        obj.delete()
        return redirect('liste.html')  # Rediriger vers une vue après suppression, par exemple la liste des Ressalles

    # Si ce n'est pas une requête POST, afficher une page de confirmation
    return render(request, 'confirm_delete.html', {'object': obj})


def salle_view(request):
    form = SalleForm() 
    
    if request.method == 'POST':
       
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('SalleForm')
    return render(request, 'ajoutSalle.html', {'form': form})
def hebergement_view(request):
    form = HebergementForm()  
    
    if request.method == 'POST':
        form = HebergementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HebergementForm')
    return render(request, 'ajoutChambre.html', {'form': form})

def calendrier(request):  
    all_events = GuestHouseEvent.objects.all()
    context = {
        "event":all_events,
    }
    return render(request,'calendrier.html',context)
 
def all_events(request):                                                                                                 
    all_events = GuestHouseEvent.objects.all()
    print(f"all_events: {all_events}")
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({    
            'id': event.id,                                                                                                  
            'title': event.title,                                                                                                                                                                                    
            'start':event.start_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start_time = request.GET.get("start", None)
    end_time = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event= GuestHouseEvent(title=str(title), start_time=start_time, end_time=end_time)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start_time = request.GET.get("start", None)
    end_time= request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event= GuestHouseEvent.objects.get(id=id)
    event.start_time= start_time
    event.end_time = end_time
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = GuestHouseEvent.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)