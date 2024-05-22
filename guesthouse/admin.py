from django.contrib import admin
from .models import Role, Client, GuestHouseEvent, Hebergement, Restauration, Historique, Notification, Reshebergement, Ressalle, Salle
# Register your models here.

admin.site.register(Role)
admin.site.register(Client)
admin.site.register(GuestHouseEvent)
admin.site.register(Hebergement)
admin.site.register(Restauration)
admin.site.register(Historique)
admin.site.register(Notification)
admin.site.register(Reshebergement)
admin.site.register(Ressalle)
admin.site.register(Salle)