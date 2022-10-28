class Joc:
    def __init__(self):
        self.name='john'

class Jucator(Joc):
    def __init__(self):
        self.name='ss'
        super().__init__()

obj=Jucator()
print(obj.name)