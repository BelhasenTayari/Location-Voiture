#declaration du classe Client
class Client:
    #constructeur du classe client
    def __init__(self,cin,nom,prenom,age,adresse,email,tel):
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.email = email
        self.tel = tel

    #Saisie d'un client
    def saisir():
        cin = input("\tsaisir le cin du client :")
        nom = input("\tsaisir le nom du client :")
        prenom = input("\tsaisir le prenom du client :")
        age = int(input("\tsaisir l'age du client : "))
        adresse = input("\tsaisir l'adresse du client :")
        email = input("\tsaisir l'email du client : ")
        tel = input("saisir le numero du tel du client : ")
        c = Client(cin,nom,prenom,age,adresse,email,tel)
        return c
    