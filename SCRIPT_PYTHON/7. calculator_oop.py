class calculator:

    def __init__(self):
        self.operator_1=self.validate_string(input('alege primul numar: '))
        self.operator_2=self.validate_string(input('alege al doilea numar: '))
        self.semn=self.validate_sign(input('alege un semn: '))
        if self.operator_2==0.0 and self.semn=='/':
            self.operator_2=self.validate_zero_division()

    def validate_string(self,operator):
        while operator.isdigit() is False:
            operator=input('alege din nou numarul: ')
        return float(operator)

    def validate_sign(self, semn):
        while semn not in ['+','-','*','/']:
            semn=input('alege semn: ')
        return semn

    def validate_zero_division(self):
        while self.operator_2==0.0:
            self.operator_2=input('alege din nou a doilea numar: ')
            if self.operator_2!=0.0:
                break
        return self.operator_2

    def adunare(self):
        return self.operator_1+self.operator_2

    def scadere(self):
        return self.operator_1-self.operator_2

    def inmultire(self):
        return self.operator_1*self.operator_2

    def impartire(self):
        return self.operator_1/self.operator_2

    def __str__(self):
        if self.semn=='+':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}"
        elif self.semn=='-':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}"
        elif self.semn=='*':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}"
        elif self.semn=='/':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.impartire()}"
        else:
            return 'operatia nu exista'

obiect_calculator= calculator()
print(obiect_calculator)