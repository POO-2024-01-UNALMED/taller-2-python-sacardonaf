class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        numeroAsientos=0
        for i in range(0,self.asientos.length()):
            if type(self.asientos[i])==Asiento:
                numeroAsientos+=1
        return numeroAsientos

    def verificarIntegridad(self):
        if self.registro==self.motor.registro:
            for j in range(0,self.asientos.length()):
                if type(self.asientos[j])==Asiento:
                    if self.registro!=self.asientos[j].registro:
                        return("Las piezas no son originales")
            return("Auto original")
        else:
            return("Las piezas no son originales")
