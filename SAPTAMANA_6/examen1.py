'''Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine. (1 punct)'''

sir_caractere= str(input("Introduceti un sir de maxim 10 caractere: "))
print(sir_caractere)

suma_vocale = 0

for i, v in enumerate(sir_caractere):
    if sir_caractere[i] == 'a' or sir_caractere[i] == 'e' or sir_caractere[i] == 'i' or sir_caractere[i] == 'o' or sir_caractere[i] == 'u':
        suma_vocale+= 1

print("suma vocalelor din sirul de caractere este=", suma_vocale)

'''Sa se scrie un program care sa calculeze impartirea dintre trei numere.
Daca valorile sunt egale, returnati de trei ori rezultatul.
Impartirea la 0 va duce la rezultatul 0.'''


# def impartire(a,b,c):
#     try:
#         if a == 0 or b == 0 or c == 0:
#             return a/b/c
#     except Exception as e:
#         print("impartirea la 0 duce la rezultatul 0", e)
#     if a == b and b == c:
#         return (a/b/c)*3
#     return a/b/c
#
# print(impartire(2,1,2))

'''Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7]. 
Sa se insereze in acest sir dupa fiecare element par, dublul acestuia'''

# sir = [1,2,3,4,5,6,7]
# sir_modificat=[]
# for i,v in enumerate(sir):
#         if sir[i]%2==1:
#             sir_modificat.append(sir[i])
#         else:
#             sir_modificat.append(sir[i])
#             sir_modificat.append(sir[i]*2)
#
# print(sir_modificat)
#


