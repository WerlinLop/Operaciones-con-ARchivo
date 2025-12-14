
def lista():
    print("1 Crear archivo")
    print("2 guardar archivo")
    print("3 leer archivo")
    print("4 actualizar nombre")
    print("5 salir ")


def crear_archivo():
    nombre= input("crea el nombre de tu archivo: ")

    with open(nombre, "w" ) as inicio:
        inicio.write("NOMBRE: \n")
        inicio.write("MATRICULA: \n")
        inicio.write("CORREO: \n")
        inicio.write("TELEFONO: \n")
    print(f"el nombre de tu programa es {nombre}")


def cambio():
    ingresar = input("ingrese el nombre del archivo: ")

    nombre = input("NOMBRE: ")
    matricula = input("matricula: ")
    correo = input("correo: ")
    telefono = input("telefono: ")
    
    with open(ingresar, "a") as g:
        g.write(f"NOMBRE: {nombre}\n")
        g.write(f"matricuala: {matricula}\n")
        g.write(f"correo: {correo}\n")
        g.write(f"telefono: {telefono}")

    
def leer_archivo():
    ingresar = input("ingrese el nombre del archivo: ")
    
    try:
        with open(ingresar, "r") as fil:
            leer= fil.read()
            print(leer)

    except:
        print("no se encuentra")

def actualizar_nombre():
    ingresar = input("ingrese el nombre del archivo: ")

    try:
        with open(ingresar, "r") as archivo:
            archivito= archivo.readlines()

        nombre_Viejo = input("NOMBRE a buscar: ")
        nuevonmre= input("nuevo NOMBRE: ")

        for i in range (len(archivito)):
            if "NOMBRE: " in archivito[i] and nombre_Viejo in archivito[i]:
                archivito[i] = f"NOMBRE: {nuevonmre}\n"
                print("nombre actulizado")
                break 
        else:
            print("no se encontro el nombre")
                    
        with open(ingresar, 'w') as archivo: 
            archivo.writelines(archivito)

    except: 
        print("error el archivo no se encuentra")


while True:
    lista()
    elepcion =input("has tu Elepcion: ")

    if elepcion == "1":
        crear_archivo()
    elif elepcion =="2":
        cambio()
    elif elepcion == "3":
        leer_archivo()
    elif elepcion == "4":
        actualizar_nombre()
    elif elepcion == "5":
        print(" hatsa luego")
        break
    else:
        print("elepcion invalida")