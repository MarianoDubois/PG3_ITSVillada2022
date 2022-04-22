class operaciones:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.srmd()

    def srmd(self):
        suma = self.n1+self.n2
        resta = self.n1-self.n2
        multiplicacion = self.n1*self.n2
        division = self.n1/self.n2
        print(suma," ",resta," ",multiplicacion," ",division)

op1=operaciones(1,2)
