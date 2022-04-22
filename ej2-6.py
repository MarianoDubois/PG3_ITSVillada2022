class familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        print(self.__str__())
    
    def __str__(self):
        hijos2 = " ".join(self.hijos)
        cadena = self.padre+" "+self.madre+" "+hijos2
        return cadena

hijos = ["manolo", "juan", "max steel"]        
f1 = familia("pedro", "juanita", hijos)
