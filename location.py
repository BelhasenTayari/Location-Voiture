#declaration du classe Location
class Location:
    n = 1
    #constructeur du classe Location
    def __init__(self,cin,matricule,dateLocation,dureeLocation,prixLocation):
        self.num = Location.n
        self.cin = cin
        self.matricule = matricule
        self.dateLocation = dateLocation
        self.dureeLocation = dureeLocation
        self.montant = dureeLocation * prixLocation
        Location.n += 1
    