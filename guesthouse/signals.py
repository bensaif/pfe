from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Reservation, Tracabilite

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_mac_address(ip):
   
    return "00:1A:2B:3C:4D:5E"  
@receiver(post_save, sender=Reservation)
def log_reservation_save(sender, instance, created, **kwargs):
    request = kwargs.get('request')
    if created:
        type_action = 'ajout'
        details_modification = ""
    else:
        type_action = 'modification'
        details_modification = "Détails de la modification"

    if request:
        ip = get_client_ip(request)
        mac = get_mac_address(ip)
    else:
        ip = '127.0.0.1'
        mac = '00:00:00:00:00:00'

    Tracabilite.objects.create(
        id_reservation=instance,
        type_action=type_action,
        adresse_ip=ip,
        adresse_mac=mac,
        details_modification=details_modification
    )

@receiver(post_delete, sender=Reservation)
def log_reservation_delete(sender, instance, **kwargs):
    request = kwargs.get('request')
    if request:
        ip = get_client_ip(request)
        mac = get_mac_address(ip)
    else:
        ip = '127.0.0.1'
        mac = '00:00:00:00:00:00'

    Tracabilite.objects.create(
        id_reservation=instance,
        type_action='suppression',
        adresse_ip=ip,
        adresse_mac=mac
    )
