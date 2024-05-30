# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone
class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_directeur = models.BooleanField(default=False)
    is_chefreception = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_financier = models.BooleanField(default=False)


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prenom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    numtel = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    email = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    adresse = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')



class GuestHouseEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Hebergement(models.Model):
    idchambre = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    prix = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    maison = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    chambre = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    etage = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    local = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')



class Historique(models.Model):
    idhistorique = models.IntegerField(primary_key=True)
    adressip = models.CharField(db_column='adressIP', max_length=45)  # Field name made lowercase.
    date = models.DateField()
    tache = models.CharField(max_length=45)



class Notification(models.Model):
    idnotification = models.IntegerField(primary_key=True)
    consulte = models.IntegerField()
    email = models.CharField(max_length=45)
class Salle(models.Model):
    idsalle = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prix = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    local = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    def __str__(self):
        return self.type

class Reshebergement(models.Model):
    idhebergement = models.AutoField(primary_key=True)
    Courrier = models.PositiveIntegerField()
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    Demandeur = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    Capacite = models.PositiveIntegerField()
    DateEntre = models.DateField(db_column='DateEntre')  # Field name made lowercase.
    DateSortie = models.DateField(db_column='DateSortie')  # Field name made lowercase.
    hebergement = models.CharField(max_length=45)  # Field name made lowercase.
    PriseenCharge = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    Moyen = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    Statut = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    Type = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    idchambre = models.ForeignKey(Hebergement, models.DO_NOTHING, db_column='idchambre')


    def __str__(self):
        return self.some_field
class Ressalle(models.Model):
    DEJEUNER_CHOICES = [
        (0, '0'),
        (1, '1'),
        
    ]

    PAUSE_CAFE_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
    ]
    idressalle = models.AutoField(primary_key=True)
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    demandeur= models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    dateEntrée = models.DateField(db_column='dateEntre')  # Field name made lowercase.
    dateSortie = models.DateField(db_column='dateSorti')  # Field name made lowercase.
    Salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    nombrePersonne = models.PositiveIntegerField(db_column='nombrePersonne')
    sujet = models.CharField(db_column='sujet', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    dejeuner = models.IntegerField()
    pauseCafe= models.IntegerField()
    courrier = models.PositiveIntegerField(db_column='Courrier')  # Field name made lowercase.
    moyen = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    priseEnCharge = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    statut = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    commentaire = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci', blank=True)
    def __str__(self):
        return f"Réservation pour {self.salle} du {self.dateEntrée} au {self.dateSortie}"




class Restauration(models.Model):
    idrestauration = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prix = models.IntegerField()





class Reservation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
class Tracabilite(models.Model):
    ACTION_CHOICES = [
        ('ajout', 'Ajout'),
        ('modification', 'Modification'),
        ('suppression', 'Suppression'),
    ]

    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    type_action = models.CharField(max_length=12, choices=ACTION_CHOICES)
    date_action = models.DateTimeField(default=timezone.now)
    adresse_ip = models.GenericIPAddressField()
    adresse_mac = models.CharField(max_length=17)
    details_modification = models.TextField(blank=True, null=True)