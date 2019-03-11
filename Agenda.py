import datetime

def es_numero(valor):
    """ Indica si un valor es numérico o no. """
    return isinstance(valor, (int, float, complex))

def es_cadena_no_vacia(valor):
    """ Indica si la cadena esta vacia o no """
    if isinstance(valor, (str)) and len(valor)>0:
        return True
    else:
        return False

class Persona(object):
    def __init__(self, nombre, apellidos, dni, edad,telefono, fechanacimiento):

        if es_cadena_no_vacia(nombre):
            self.nombre = nombre
        else:
            raise TypeError("El nombre debe ser una cadena no vacía")
        if es_cadena_no_vacia(apellidos):
            self.apellidos = apellidos
        else:
            raise TypeError("El nombre debe ser una cadena no vacía")
        if es_cadena_no_vacia(dni):
            self.dni = dni
        else:
            raise TypeError("El nombre debe ser una cadena no vacía")

        if es_numero(edad):
            self.edad = edad
        else:
            raise TypeError("El nombre debe ser un numero")
        if es_numero(telefono):
            self.telefono = telefono
        else:
            raise TypeError("El nombre debe ser un numero")


        self.fechanacimiento = fechanacimiento

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getDni(self):
        return self.dni

    def getEdad(self):
        return (self.edad)

    def getTelefono(self):
        return self.telefono

    def getFechaNacimiento(self):
        return self.fechanacimiento
    def __str__(self):

        return self.nombre+" "+self.apellidos+" "+self.dni+" "+str(self.edad)+" "+str(self.telefono)+" "+self.fechanacimiento.strftime("%x")


def mostrarContactos(contactos):
    for i in range(1, len(contactos)):
        print(contactos.__getitem__(i))


def buscarNombre(contactos,nombre):
    for i in range(1, len(contactos)):
        if contactos.__getitem__(i).nombre == nombre:
            print(contactos.__getitem__(i))

def buscaApellidos(contactos,apellido):
    for i in range(1, len(contactos)):
        if contactos.__getitem__(i).apellidos == apellido:
            print(contactos.__getitem__(i))
def buscaDNI(contactos,dni):
    for i in range(1, len(contactos)):
        if contactos.__getitem__(i).dni ==dni:
            print(contactos.__getitem__(i))
def buscaEdad(contactos,edad):
    for i in range(1, len(contactos)):
        if contactos.__getitem__(i).edad == edad:
            print(contactos.__getitem__(i))


def calculate_birth(original_date):
    date1 = datetime.datetime.now()
    date2 = datetime.datetime(date1.year, original_date.month, original_date.day)
    delta = date2 - date1
    days = delta.total_seconds() / 60 /60 /24

    print(days," dias quedan para que sea su cumpleaños")

contactos=[""]


p1 = Persona("Pepe","Vidal","20925473G",2,198123123, datetime.datetime(1999,6,4))
p2 = Persona("Jose","Belles","40925473G",5,987456234, datetime.datetime(2013,3,2))
contactos.append(p1)
contactos.append(p2)

mostrarContactos(contactos)



buscarNombre(contactos,"Pepe")
buscaApellidos(contactos,"Belles")
buscaDNI(contactos,"20925473G")
buscaEdad(contactos,2)
calculate_birth(p1.fechanacimiento)