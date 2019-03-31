import datetime

class Persona:
    def __init__(self, madre, padre):
        self.madre = madre
        self.padre = padre
        self.edad = 0
        self._vivo = True
        self._nombre = ""
        self._eventos = []
        self._agregarEvento("Nació")
    
    def _agregarEvento(self, que):
        ahora = datetime.datetime.now()
        self._eventos.append(str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second) + " - " + que)

    
    def obtenerEdad(self):
        return edad
    
    def cumplirAnios(self):
        if self._vivo:
            self.edad = self.edad + 1
            self._agregarEvento("Cumplió años. Ahora tiene " + str(self.edad))
            
    def esHuerfano(self):
        loes = True
        if self.madre != None:
            if self.madre.estaVivo():
                loes = False
        if self.padre != None:
            if self.padre.estaVivo():
                loes = False
        
        if loes:        
            self._agregarEvento("Descubrió que es huérfano")
        else:
            self._agregarEvento("Está feliz porque no es huérfano")
        return loes
    
    def morir(self):
        self._vivo = False
        self._agregarEvento("Murió")
    
    def bautizar(self, nombre, apellido):
        if self._nombre == "":
            self._nombre = nombre
            self._apellido = apellido
            self._agregarEvento("Fue bautizado con el nombre " + nombre + " y apellido " + apellido)
        else:
            self._agregarEvento("Lo quisieron bautiza con el nombre " + nombre + " y apellido " + apellido + " pero ya se llamaba " + self._nombre + " " + self._apellido)
    
    def estaVivo(self):
        return self._vivo
        
    def esHermanoDe(self, otraPersona):
        padresOtra = []
        
        if otraPersona.padre != None:
            padresOtra.append(otraPersona.padre)
        if otraPersona.madre != None:
            padresOtra.append(otraPersona.madre)
        
        if self.madre != None:
            if padresOtra.count(self.madre) != 0:
                self._agregarEvento("Averiguó que es hermano de " + str(otraPersona))
                return True
        if self.padre != None:
            if padresOtra.count(self.padre) != 0:
                self._agregarEvento("Averiguó que es hermano de " + str(otraPersona))
                return True
        
        self._agregarEvento("Averiguó que no es hermano de " + str(otraPersona))
        return False
        
    def obtenerHistoria(self):
        return self._eventos
    
    def __str__(self):
        if self.estaVivo():
            if self._nombre != "":
                return self._nombre + " " + self._apellido + " (" + str(self.edad) + ")"
            else:
                return "Anónimo (" + str(self.edad) + ")"
        else:
            if self._nombre != "":
                return self._nombre + " " + self._apellido + " (QEPD)"
            else:
                return "Anónimo (QEPD)"                


p1 = Persona(None, None)
p1.bautizar("Alberto", "Garcia")
p1.cumplirAnios()
p1.cumplirAnios()
p2 = Persona(None, None)
p2.bautizar("Samanta", "Carter")
p2.bautizar("Arantxa", "Sanchez")
p2.cumplirAnios()
p2.cumplirAnios()
p2.esHuerfano()
p1.morir()
p3 = Persona(p1, p2)
p3.bautizar("Serafin", "García")
p3.esHuerfano()
p1.morir();
p3.esHuerfano()
p2.morir();
p3.esHuerfano()
p3.esHermanoDe(p2)
p4 = Persona(p1, p2)
p4.bautizar("Ferdinando", "García")
p4.cumplirAnios()
p4.cumplirAnios()
p4.cumplirAnios()
p4.cumplirAnios()
p4.cumplirAnios()
p4.cumplirAnios()
p3.esHermanoDe(p4)

print(*p2.obtenerHistoria(), sep='\n')
print(*p3.obtenerHistoria(), sep='\n')
                
                