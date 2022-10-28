# class Dog:
#
#     legs_no=4 # variabila de clasa/ atribut de clasa
#
#     def __init__(self, name):
#         self.__name=name
#
#     @property
#     def nume(self):
#         return self.__name
#
#     @nume_de_familie.setter
#     def nume_de_familie(self,prenume):
#         self.__name=prenume
#
#     @nume_de_familie.deleter
#     def nume_de_familie(self):
#         del self.__name
#
#     # @staticmethod
#     # def speak():
#     #     return "ham ham"
#
#     def __str__(self):
#         return str(self.name)
#
#     # def change_name(self,name):
#     #     self.name=name
#     #     return self.name
#
# caine=Dog("rex")
# rasa=Dog("max")
# print(caine.nume_de_familie)
# caine.nume='Jon'
# print(caine.nume)
# del caine.nume_de_familie
# print(caine.nume_de_familie)
# print(caine)
# print(caine.legs_no, Dog.legs_no)
# print(rasa)
# print(caine.change_name("rex1"))
# Dog.legs_no=2
# caine.legs_no=3
# #Dog.legs_no=3
# print('rasa', rasa.legs_no,'legs no class', Dog.legs_no)
# print('caine', caine.legs_no, 'legs no class', Dog.legs_no)
# print(caine.name)
# print(caine.speak())
# print(caine._Dog__nume)

# def decorator_simplu(parametru):
#     print(f"apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#     return "buna seara"
#
# @decorator_simplu
# def functie_complexa():
#     return"noapte buna"
#
# # print (functie_simpla())
#
# print(functie_complexa())

# def decorator_depozit(functia_noastra):
#     def ambalaj(carti):
#         return f"ambalam produse din {functia_noastra.__name__} cu {carti}"
#     return ambalaj
#
# @decorator_depozit
# def impachetare_carti(args):
#     return args


# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*carte):
#             return f"ambalam produse din {functia_noastra.__name__} cu {material} care contine cartea {carte}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume
#
# print(impachetare_carti("amintiri din copilarie","baltagul"))
# print(impachetare_carti("amintiri din copilarie","baltagul"))


# def decorator(simbol):
#     def adauga_simbol(functie):
#         def functie_upper(parametru):
#             return parametru.upper() + simbol
#         return functie_upper
#     return adauga_simbol
#
# @decorator(".")
# def functie(propozitie):
#     return propozitie
#
# print(functie("ana are mere"))
import time

def calculeaza_timpul(functia):
    def functie_interioara(*param):
        inceput=time.time()
        functia(*param)
        sfarsit=time.time()
        return f"timp total de executie:{sfarsit-inceput}"
    return functie_interioara

@calculeaza_timpul
def adunare(*args):
    suma=0
    for i in args:
        suma+=i
    print(suma)
    return suma

print(adunare(1,2,3))




