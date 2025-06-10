
class Estudiante:
    def __init__(self,cif="",nom="",prom=0.0,beca=-1,sex=False):
        self.cif=cif
        self.nombre=nom
        self.promedio=prom
        self.becado=beca
        self.sexo=sex
    
    # Guarda los datos del estudiante en un fichero en disco
    def guardar(self):
        fichero=open("Estudiantes.dat","a")
        fichero.write(f"{self.cif} {self.nombre}\t {self.promedio} {self.becado} {self.sexo}\n")
        fichero.close()
    
    def leer(self,cif):
        fichero=open("Estudiantes.dat", "r")
        flag=True
        while flag:
            linea= fichero.readline()
            if (linea==""): flag= False
            else:
                partes= linea.strip().split()
                if (partes[0] == cif):
                    self.cif = partes[0]
                    self.nombre = ' '.join(partes[1:-3])
                    self.promedio = float(partes[-3])
                    self.becado = int(partes[-2])
                    self.sexo = partes[-1] == 'True'
                    flag = False
        fichero.close()
        

        
    
    
    