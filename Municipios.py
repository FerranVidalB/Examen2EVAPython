


def municipiosMenosMujeres():
    with open("DatosPoblacionCastellon2018.csv", 'r') as f:
        line = f.readline()
        while line:
            words = line.split(";")
            if words[1] > words[2]:
                print(words[0][6:])
            line = f.readline()
def mostrarPoblacion():
    nombre= input("Introduzca el nombre de la poblacion")

    with open("DatosPoblacionCastellon2018.csv", 'r') as f:
            line = f.readline()
            while line:
                words = line.split(";")
                if words[0][6:] == nombre:
                    print("el municipio "+nombre+" contiene "+words[1]+" hombres y "+words[2]+" mujeres")
                line = f.readline()


def indicarDatoPoblacion():
    numHabitantes =  input("Introduzca el numero de habitantes que desea realizar la consulta")
    operacion = input(" escriba '>' para consultar los que contienen mas poblacion o '<' para el resto")

    with open("DatosPoblacionCastellon2018.csv", 'r') as f:
            line = f.readline()
            out=""
            while line:
                words = line.split(";")
                habitantes =float(words[1])+ float(words[2])

                if operacion == ">":
                    if float(numHabitantes) < habitantes:
                        out += words[0][6:]+" es mayor que "+numHabitantes+"\n"
                if operacion =="<":
                    if float(numHabitantes) > habitantes:
                        out += words[0][6:] + " es menor que " + numHabitantes + "\n"

                line = f.readline()
    with open("fichero2.txt", 'w+') as f2:
        f2.write(out)


i=1
while(i!=0):
    i= input("1 consultar Municipios con menos mujeres, 2 consultar poblacion, 3 indicar un dato de poblacion 0 para salir")
    if i == "1":
        municipiosMenosMujeres()
    if i =="2":
        mostrarPoblacion()
    if i =="3":
        indicarDatoPoblacion()