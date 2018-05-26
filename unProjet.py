class personne:

    def __new__(cls, name, surname, rang):
        print("Appelle de la methode __new__ de la class {}".format(cls))

        return object.__new__(cls)

    def __init__(self, name, surname, rang):
        self.nom = name.upper()
        self.prenom = surname.capitalize()
        self.classe = rang

    def __str__(self):
        return "Salut {} {} tu est actuellement en {}".format(self.nom, self.prenom, self.classe)
    pass


user1 = personne("delar","EMMARIO","1ere anne de licence informatique")
print(user1)
