class real:
    def __init__(self, name, monAge):
        self.nom = name
        self.age = monAge


class personne(real):

    def __init__(self, name, cle, nom_attr, val_attr):
        self.nom = name
        self.mdp = cle
        object.__setattr__(self, nom_attr, val_attr)

    def __getattr__(self, age):
        print("il n'y a pas d'attribut {} dans la class personne".format(age))

    def __setattr__(self, nom_attr, val_attr):
        object.__setattr__(self, nom_attr, val_attr)
        print(self.__dict__)

    def __repr__(self):
        return "nom : {}, mdp : {}".format(self.nom, self.mdp)

    def __gt__(self, autreObj):
        return self.age > autreObj.age


'#def of obj'
user1 = personne("marc", "monMdp", "age", 20)
user2 = personne("marc", "monMdp", "age", 21)

'#test'
print(user1.age)
print(user1)

print(user2.__gt__(user1))
user1.__setattr__("prenom", "emmario")
print(issubclass(personne, real))
