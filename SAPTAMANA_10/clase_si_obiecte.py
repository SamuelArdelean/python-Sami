#Max este o pisica mare care doarme toata ziua.
#object name = Max (substantiv)
#class name = Pisica (substantiv)
#property = marime_pisica (mare) (adjectiv)
#activity = doarme (verb)

#O masina Dacia merge repede.
#objectname = Dacia
#class name = masina
#property = repede
#activity= merge

# Catelul Max are 4 picioare si latra tare.
# object name = Max
# class = Catelul
# property = 4 picioare, tare
# activity = latra
#
# class Dog:
#     pass
#
# obiect_1= Dog()
# print(obiect_1)

# stack = []
#
# def push(val):
#     stack.append(val)
#
# push(3)
# push(2)
# push(1)
# print(stack)
#
# def pop():
#     valoare= stack[-1]
#     del stack[-1]
#     return valoare
#
# print(pop())
# print(pop())
# print(pop())

# class Stack:
#
#     def __init__(self,val1):
#         self.__stackList =[]
#         self.valoare1= val1
#
#     def push(self):
#         self.__stackList.append(self.valoare1)
#         print(self.__stackList)
#
#     def pop(self):
#         valoare=self.__stackList[-1]
#         def self.__stackList[-1]
#         return valoare
#
#
# obiect_stiva = Stack(3)
# obiect_stiva_1=Stack(2)
# obiect_stiva_2=Stack(1)
#
# obiect_stiva.push()
# obiect_stiva_1.push()
# obiect_stiva_2.push()
#
# class Dog:
#     pass
#
# obiect_1= Dog()
# print(obiect_1)

# stackList = []
# def push(val):
#     stack.append(val)
#
# push(3)
# push(2)
# push(1)
# print(stackList)
#
# def pop():
#     valoare = stackList[-1]
#     del stackList[-1]
#     return valoare
#
# print(pop())
# print(pop())
# print(pop())

class Stack:

    def __init__(self, val1):
        #print("hi")
        self.__stackList=[]
        self.valoare1 = val1

    def push(self):
        self.__stackList.append(self.valoare1)
        #print(self.valoare1)
        print(self.__stackList)

    def pop(self):
        valoare= self.__stackList[-1]
        del self.__stackList[-1]
        return valoare
obiect_stiva= Stack(3)
# obiect_stiva_1= Stack(2)
# obiect_stiva_2= Stack(1)
#print(obiect_stiva.__stackList)
obiect_stiva.push()
obiect_stiva.push()
obiect_stiva.push()
# obiect_stiva_1.push()
# obiect_stiva_2.push()

print(obiect_stiva.pop())
# print(obiect_stiva_1.pop())
# print(obiect_stiva_2.pop())