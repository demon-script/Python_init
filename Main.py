
class Master:
    """
    Clase contendora.
    
    Esta clase es para ensayar
    No tiene atributos
    tiene un método
    """ 
    
    def suma(self,a,b):
        """
        Metodo suma.
        
        Esta función recibe como parámetros...
        @param a: Int
        @param b: Int
        
        @return: None
         
        """
        print(a+b)

print("Hello Demon!!!")
obj = Master
print(obj.suma.__doc__)
print("Ahora imprimimos el Docstring de la Clae...")
print(Master.__doc__)
print("Ahora mostramos lo mismo con help...")
help(obj.suma.__doc__)