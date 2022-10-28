'''PROGRAMARE CONDITIONATA'''
# - structurile decizionale evalueaza mai multe expresii care au o valoare booleana: True sau False
# - pentru luarea unei decizii poate fi folosita DOAR instructiunea if, ramura else fiind optionala
# - pentru insiruirea ramurilor decizionale se fooseste if....elif

'''1. CONDITIA IF'''
#varsta = int(input("va rugam sa introduceti varsta dvs:"))
#if varsta >= 18:
#    print("sunteti eligibil pentru scoala de soferi")
#else:
#    print("sunteti eligibil doar dupa varsta de 18 ani")
#    if varsta == 17:
#        print("mai aveti un an pentru a fi eligibil")

#if varsta>= 65:
#    print("varsta pensionare")
#elif varsta >=15:
#    print("varsta liceu")
#elif varsta >=25:
#    print("varsta facultate")
#else:
#    print("esti micut!")

#a = 1
#b = 2
#impartire = 0
#if a > 0 and b > 0 and (impartire := a / b) and impartire > 1:
 #   print(impartire)
#if a > 0 and b > 0 and a / b > 1:
#    impartire = a / b
#    print(impartire)

'''2. CONDITIA WHILE'''
#WHILE

# print('primul print')
# i = 0
# while i < 3:
#     print('se respecta conditia')
#     print('valoarea este: ' + str(i))
#     i += 1
#     #i = i+1
# print(' am ajuns la sfarsit')

'''3. CONDITIA FOR'''
#FOR - repeta un set de instructiuni de un numar cunoscut si finit de pasi
#import random
#
# for i in range(10):
#     print(f'Set Instructiuni [{i+1}]')

# sir = "ana are mere"
# sir1 = list(sir)
# print(sir1)
# for i, v in enumerate(sir):     #i= index, v= valoare
#     print(i, '=>>', v)
#
# for variabila_temporara in range(2, len(sir), 3):
#     print(variabila_temporara, '=>>', sir[variabila_temporara])

# dictionar = {'1': 'val1', "2": "val2","3": "val3"}
# print(dictionar["2"])
# print(dictionar)
# dictionar.update({4:"val4"})
# dictionar[5] = 'val5'
# dictionar.update({"3":'val300'})
# for i in dictionar.keys():
#     print(i)
# print(dictionar)
#
# for i in dictionar:
#     print(i, '->>', dictionar[i])
# print(dictionar)


'''4. BREAK SI PASS'''
# BREAK- opreste executia buclei si transfera controul catre urmatoarea instructiune din afara buclei
# while True:
#     random_choice = random.choice([0,1,2,3,4,5,6,7,8,9,10])
#     if random_choice % 3 == 0:
#         break
#     print(f'random_choice = {random_choice}')

# PASS - are rol de placeholder. Nu are absolut nicio actiune, doar substituie continutul unui bloc pentru
# a permite scrierea acestuia, dar necompletarea lui cu instructiuni

# if True:
#     pass

