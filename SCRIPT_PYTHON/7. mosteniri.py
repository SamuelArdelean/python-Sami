# class Exemplu:
#     def __init__(self,val=1):
#         self.__first=val
#
#     def set_second(self, valoare):
#         self.second=valoare
#         return self.second
#
# obiect_1=Exemplu()
# print(obiect_1)
# print(obiect_1.set_second(4))
#
# obiect_2=Exemplu(2)
#
#
# print(obiect_1.__dict__)
# print(obiect_2.__dict__)

# class Exemplu:
#     __counter=0
#
#     def __init__(self, val=1):
#         # self.__first= val
#         # Exemplu.__counter+=1
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1
#
# obiect_1=Exemplu()
# print(obiect_1.a)
# print(obiect_1.b)
# obiect_2=Exemplu(2)
# obiect_3=Exemplu(4)

# print(obiect_1.__dict__, obiect_1._Exemplu__counter)
# print(obiect_2.__dict__, obiect_2._Exemplu__counter)
# print(obiect_3.__dict__, obiect_3._Exemplu__counter)

class Super:

    def __init__(self, name= 'sami'):
        self.nume=name

    def __str__(self):
        return f'numele meu este {self.nume}'

class Sub(Super):

    def __init__(self, name= 'ardelean'):
        super().__init__(name)
        pass

obiect= Sub()
print(obiect)
