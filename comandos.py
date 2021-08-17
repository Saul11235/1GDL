class Comandos:
    def __init__(self):
        self.comando=""
        self.argumentos=[]
        
    def LeerExterno(self,ruta):
        print("se ha leido externo)")


if __name__=="main":
    a=Comandos()
    a.LeerExterno("Ejemplo.SDOF")
