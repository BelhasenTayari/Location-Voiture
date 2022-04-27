from datetime import datetime
from datetime import date
from client import Client
from voiture import Voiture
from location import Location
from datetime import timedelta
import os.path


#declaration du classe Agence
class Agence:

    #Constructeur du classe Agence
    def __init__(self):
        self.voitures = {}
        self.clients = {}
        self.locations = {}

    #********//Gestion des Voitures//**************
 
    #-------------------------------------------------
    #Mise A jour des voitures

    #ajouter une voiture
    def ajouterVoiture(self,v):
        if(v.matricule in self.voitures.keys()):
            print("La Voiture est Deja existe !")
        else:
            self.voitures[v.matricule] = v
    
    #Suppression des Voitures
    
    #suppression d'une voiture donnees
    def supprimerVoiture(self, matricule):
        if(matricule in self.voitures.keys() ):
            del self.voitures[matricule]
        else:
            print("la voiture n'existe pas !")
    
    #suppression des voitures d'une marque donnees
    def supprimerVoituresParMarque(self, marque):
        l = list(self.voitures.keys())
        for i in l:
            if(self.voitures[i].marque == marque):
                del self.voitures[i]
    
    #suppression des voitures (agé>10ans)
    def supprimerVoituresParAge(self):
        l = list(self.voitures.keys())
        for i in l:
            v = self.voitures[i]
            duree = years_between(v.dateAchat, str(date.today()))
            if(duree>10):
                del self.voitures[i]

    #Modification d'une voiture donnees
    
    #modification par prix
    def modifierPrixVoiture(self,matricule):
        if(matricule in self.voitures.keys()):
            nouveauxPrix = float(input("saisir le nouveau prix pour la voiture " + matricule + " : "))
            self.voitures[matricule].prixLocation = nouveauxPrix
        else:
            print("voiture n'existe pas pour le modifier")
    
    #----------------------------------------------------
    #Recherche et affichage des voitures

    #affichage de tous les voitures
    def afficherVoitures(self):
        for i in self.voitures.values():
            i.afficher()
    
    #affichage voiture par matricule
    def afficherMatriculeDonnees(self, matricule):
        if(matricule in self.voitures.keys()):
            self.voitures[matricule].afficher()
        else:
            print("voiture avec matricule " + matricule + " n'existe pas !")

    #affichage voiture par marque
    def afficherVoitureParMarque(self,marque):
        for i in self.voitures.values():
            if(i.marque == marque):
                i.afficher()
            
    #affichage voiture par couleur
    def afficherVoitureParCouleur(self,couleur):
        for i in self.voitures.values():
            if(i.couleur == couleur):
                i.afficher()
    
    #affichage des voitures disponibles
    def afficherVoituresDisponibles(self):
        for i in self.voitures.values():
            if(i.etat):
                i.afficher()

    #affichage des voitures loué
    def afficherVoituresDisponibles(self):
        for i in self.voitures.values():
            if not(i.etat):
                i.afficher()

    #affichage des voitures loué entre deux dates
    def afficherVoituresLoueEntreDeuxDates():
        pass


    #***********//Gestion des Clients//************
    
    #Mise a jour
    #ajouter un client
    def ajouterClient(self, c):
        if(c.cin in self.clients.keys()):
            print("le client est existe deja !")
        else:
            self.clients[c.cin] = c
    
    #suppression d'un client
    def supprimerClient(self, cin):
        if(cin in self.clients.keys()):
            del self.clients[cin]
        else:
            print("client du numero cin = "+cin+ " n'existe pas !")
    
    #Modifier les donnees d'un client

    #modification d'adresse du client
    def modifierAdresseClient(self, cin):
        if(cin in self.clients.keys()):
            adresse = input("saisir la nouvelle adresse du " + cin + " : ")
            self.clients[cin].adresse = adresse
        else:
            print("client n'existe pas !")
    
    #modification du numero du tel du Client
    def modifierTelClient(self, cin):
        if(cin in self.clients.keys()):
            tel = input("saisir le nouveau num de tel du" + cin + " : ")
            self.clients[cin].tel = tel
        else:
            print("client n'existe pas !")
        
    #modification du mail du client
    def modifierEmailClient(self, cin):
        if(cin in self.clients.keys()):
            email = input("saisir le nouveau email du" + cin + " : ")
            self.clients[cin].email = email
        else:
            print("client n'existe pas !")

    #Recherche et affichage des clients
    
    #affichage de tous les clients
    def afficherTousLesClient(self):
        for i in self.clients.values():
            i.afficher()
    
    #affichage d'un client donnees
    def afficherClientDonnees(self, cin):
        if(cin in self.clients.keys()):
            self.clients[cin].afficher()
        else:
            print("client " + cin + " n'existe pas ! ")
    

    #***********//Gestion des locations//**************

    #Mise a jour 
    
    #ajouter une location
    def ajouterLocation(self, l):
        if(l.num in self.locations.keys()):
            print("Location deja existe avec ce numero : "+l.num)
        else:
            self.locations[l.num] = l
    
    #suppression d'une location
    def supprimerLocation(self, num):
        if(num in self.locations.keys()):
            del self.locations[num]
        else:
            print("location avec le numero "+str(num) +" n'existe pas")

    #modification des Location

    #modification du Date du location
    def modifierDateLocation(self,num):
        if(num in self.locations.keys()):
            dateLoc = input("saisir la nouvelle date de location : ")
            self.locations[num].dateLocation = dateLoc
        else:
            print("location avec le numero "+str(num) +" n'existe pas")
    
    #modification du duree du location
    def modifierDateLocation(self,num):
        if(num in self.locations.keys()):
            duree = int(input("saisir la nouvelle duree de location : "))
            self.locations[num].dureeLocation = duree
        else:
            print("location avec le numero "+str(num) +" n'existe pas")
    

    #*************//Enregistrement et chargement//*****************
    #enregistrement des voitures dans un fichier
    def enregistrerVoituresDansFichier(self):
        f = open("voitures.txt","w")
        for i in self.voitures.values():
            ch = i.matricule +"|"+i.marque+"|"+i.couleur+"|"+str(i.etat)+"|"+i.dateAchat+"|"+str(i.prixLocation)+"\n"
            f.write(ch)
        f.close()
    
    
    #chargement des voitures depuis un fichier
    def chargerVoituresDepuisFicher(self):
        f = open("voitures.txt","r")
        ch = f.read()
        l = ch.split("\n")
        l = l[0:len(l)-1]
        voitures = []
        for i in l:
            k = i.split("|")
            voitures = voitures + [Voiture(k[0], k[1],k[2],(k[3] == "True"), k[4], float(k[5]))]
        f.close()

        for i in voitures:
            self.ajouterVoiture(i)
        

    #enregistrement des clients dans un fichier
    def enregistrerClientsDansFichier(self):
        f = open("clients.txt","w")
        for i in self.clients.values():
            ch = i.cin +"|"+i.nom+"|"+i.prenom+"|"+str(i.age)+"|"+i.adresse+"|"+i.email+"|"+i.tel+"\n"
            f.write(ch)
        f.close()
    
    #chargement des Client depuis un fichier
    def chargerClientsDepuisFichier(self):
        f = open("clients.txt","r")
        ch = f.read()
        l = ch.split("\n")
        l = l[0:len(l)-1]
        clients = []
        for i in l:
            k = i.split("|")
            clients = clients + [Client(k[0], k[1],k[2],int(k[3]) , k[4], k[5], k[6])]
        f.close()

        for i in clients:
            self.ajouterClient(i)


    #enregistrement des locations dans un fichier
    def enregistrerLocationsDansFichier(self):
        f = open("locations.txt","w")
        for i in self.locations.values():
            ch = str(i.num) +"|"+i.cin+"|"+i.matricule+"|"+i.dateLocation+"|"+str(i.dureeLocation)+"|"+str(i.montant)+"\n"
            f.write(ch)
        f.close()

    #chargement des locations depuis un fichier
    def chargerLocationsDepuisFichier(self):
        f = open("locations.txt","r")
        ch = f.read()
        l = ch.split("\n")
        l = l[0:len(l)-1]
        locations = []
        for i in l:
            k = i.split("|")
            prix = float(self.voitures[k[2]].prixLocation)
            locations = locations + [Location(k[1],k[2],k[3], int(k[4]), prix)]
        f.close()

        for i in locations:
            self.ajouterLocation(i)


    
    #File exist
    def fileExist(self,path):
        file_exists = os.path.exists(path)
        return file_exists

    #Fonction qui teste si une voiture est disponible pendant une durée du temps
    def disponible(self,matricule,dateLocation,dureeLocation):
        dateDebut = datetime.strptime(dateLocation, "%Y-%m-%d")
        dateFin = dateDebut + timedelta(days=int(dureeLocation))

        v = self.voitures[matricule]

        for i in self.locations.values():
            if i.matricule == v.matricule:
                d = datetime.strptime(i.dateLocation, "%Y-%m-%d")
                df = d + timedelta(days=i.dureeLocation)
                if not ((dateDebut>=df)or(d>=dateFin)):
                    return False
        return True



#fonction non membre qui calcule la difference entre deux dates donnees selon les jours
def years_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days // 365)
