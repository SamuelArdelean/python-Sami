import datetime

def validare(variabila):
    """

    :param variabila: CNPul introdus de utilizator de la tastatura
    :return: CNP-ul valid
    """
    while len(variabila) != 13 or variabila.isdigit() is False:
        variabila = input("reintrodu CNP-ul: ")
    return variabila

def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet < 47:
        return True
    elif judet == (51 or 52):
        return True
    elif judet != (47 and 48 and 49 and 50):
        return False
    else:
        return False

def validare_sex(a):
    if int(a[0]) in range(1, 10):
        return True
    return False


def validare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')  #primul datetime este pachetul de date calendaristice
        return True
    except Exception:  #clasa generala care contine toate exceptiile standard din python, modalitate de a trata erorile din cod
        return False


def validator_cnp(cnp):
    """
    :param cnp: cnp-ul introdus de utilizator de la tastatura
    :return: mesaj "valid" in cazul in care cnp-ul este valid; "invalid" in cazul in care cnp-ul nu e valid
    """
    if cnp and validare_sex(cnp) and validare_data_nastere(cnp) and validare_judet(cnp):
        return "valid"
    return "invalid"

variabila_cnp = validare(input("introdu CNP-ul: "))
validator = validator_cnp(variabila_cnp)
print(validator)

