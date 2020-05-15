from random import randint;

class Motor():
    def __init__(self, id, modelo):
        self.id     = id;
        self.modelo = modelo;
    
    #GET
    def getId(self):
        return self.id;

    def getModelo(self):
        return self.modelo;
    
    #SET
    def setId(self, id):
        self.id = id;
    
    def setModelo(self, modelo):
        self.modelo = modelo;

class Carro():
    def __init__(self, id, modelo, motor):
        self.id     = id;
        self.modelo = modelo;
        self.motor  = Motor(randint(0,9), motor);
    
    #GET CARRO
    def getId(self):
        return self.id;
    
    def getModelo(self):
        return self.modelo;

    #GET MOTOR
    def getMotor(self):
        return self.motor.getModelo();
    
    def getIdMotor(self):
        return self.motor.getId();
    
    #SET MOTOR
    def setMotor(self, motor):
        self.motor.setModelo(motor);
    
    def setIdMotor(self, id):
        self.motor.setId(id);

    #SET CARRO
    def setId(self, id):
        self.id = id;
    
    def setModelo(self, modelo):
        self.modelo = modelo;