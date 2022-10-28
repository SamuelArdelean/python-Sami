print("Hello, World!")

'''I NUMERE- int, float, complex'''
#int()- intregi
#float()- zecimale
#complex()- complexe (1j,3+5j)
# type() - aflam tipul datei/ valorii
#print(type(20))

#float * float -> float
#float * integer -> float
#integer * integer -> integer
'''II OPERATORI- aritmetici, de comparare, logici, de identitate, de apartenenta, de biti'''
# 1. OPERATORI ARITMETICI
#     ADUNARE, SCADERE, INMULTRE, IMPARTIRE
#     MODUL - %- iti da restul impartitii
#     RIDICARE LA PUTERE - **
    # IMPARTIRE EXACTA - // -> iti da catul, nu restul

# 2. OPERATORI DE COMPARARE
#     ==,!=, >, <, >=, <=
#     ORICE OPERATOR DE COMPARATIE VA AVEA CA REZULTAT O DATA DE TIP BOOLEAN
#     TRUE- daca rezultatul comparatiei e adevarat
#     FALSE- nu e adevarat

# 3. OPERATORI LOGICI
#     and - evaluat ca True daca ambele sunt indeplinite, altfel False
#     or - evaluat ca True daca cel putin una e adevarata, alfe ca False
#     not - evaluat ca True daca nu e adevarata

# 4. OPERATORI DE IDENTITATE
#     is - este True daca ambele valori reprezinta aceeasi locatie de memorie, altfel False
#     is not - este True daca nu reprezinta.....
#
# 5. OPERATORI DE APARTENENTA
#     in - este True daca secventa evaluata face parte din obiect  ex 1 in [1,2,3]
#     not in - este True daca nu face parte...  ex 'a' not in 'python'
#
# 5. OPERATORI PE BITI
#     &- AND - ia val 1 daca amii biti au valarea, altfel 0
#     | - OR - ia val 1 daca cel putin unul este 1....

'''III VARIABILE'''
# - numele variabilei trebuie sa inceapa cu litera mica, nu poate incepe cu o cifra
# - poate contine orice caracter si semnul underscore _
#
# 1. VARIABILE DE ASIGNARE
# a = 3
# b = 7

#child_age = 3
#print(id(child_age))
#
# - in Python fiecare obiect este identificat printr-un ID unic
# - acest ID este asignat obiectului cand e creat
# - reprezinta adresa locatiei de memorie unde valoarea este stocata

#x = 1
#y = 3
#x = x + y
#print(x)

#x= 1
#y = 3
#x += y - modalitate diferita de a calcula suma
#print(x)

#+=/ -=/ /= / *= - alternativele la cele clasice

#first_number = 1
#first_Number = first_number + 1
#print(first_Number)

'''IV. SIRURI DE CARACTERE'''
#
# - tip de data string
# - definit intre '' sau ""
# print("Hello, World!")
#
# mesaj = "Ana are mere"
# print(mesaj)
#
# 1. SIRURI DE CARACTERE- ASCII
# - un sir de caractere poate contine orice caracter din codul ASCII
# - orice caracter din codul ASCII poate fi reprezentat printr-un numar intreg
# - pentru a obtine codul ASCII  al unui caracter:
# print(ord('a'))

# - pentru a obtine caracterul reprezentat de un cod ASCII
# print(chr(97))
#
# 2. SIRURI DE CARACTERE- ESCAPING
# - pentru folosirea ghilimelelor speciale, cu rol de caractere integrate in strung-ul nostru, folosim \ pt a face escape

#print("Si Dumnezeu a zis:\"Sa se faca lumina!\"")
#
# 3. SIRURI DE CARACTERE - MULTILINE STRING
# - pentru scrierea pe mai multe linii: newline (\n)
# print("Somnoroase pasarele \nPe la cuiburi se aduna")
# - sau folosirea ghilimelelor triple (simple sau duble)
# print("""somnoroase pasarele
# Pe la cuiburi se aduna""")

# 3. SIRURI DE CARACTERE - RAW STRING
# print("Somnoroase pasarele \nPe la cuiburi se aduna")
# print(r'somnoroase pasare,\nPe la cuiburi se aduna')  - ne ajuta cand dorim sa afisam un text asa cu este, fara a il
# formata

# 4. SIRURI DE CARACTERE - FORMATTING
# format() - definirea placeholderului se face intre {}
#print(F'for only {49} dollars! {"Have a great day!"}') # -  folosing F- strings, modaltate usoara de formatare

