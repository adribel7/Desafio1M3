agenda={}
Consulta= True
op=0
while Consulta:
    print ()
    print("AGENDA")
    print("-------------------------------------")
    print("1- Ingresar un nuevo contacto")
    print("2- Buscar contacto por nombre y apellido")
    print("3- Salir")
    print("-------------------------------------")
    op=int(input("Elija una opción: "))
    if (op==3):
        Consulta=False
        print()
        print("Saliendo")
    elif(op==1):
        contacto=input("Ingrese el nombre y apellido: ")
        if contacto in agenda.keys():
            print(f"El contacto {contacto} tiene como teléfono: {agenda[contacto]}")
        else:
            print(f"El contacto {contacto} no se encuentra en su lista, desea agregarlo??")
            op = input("1:si o 2:no\t")
            if op == '1':
                numero = input("Ingrese el numero de telefono: \t")
                agenda[contacto] = numero
                print("Contacto agregado correctamente!!!")
    else:
        (op==2)
        contacto=input("Ingrese el nombre y apellido: ")
        if contacto not in agenda:
            print("Ese contacto no existe.")
        else:
            numero=agenda[contacto]
            print("Contacto:",contacto ,"/Teléfono:", numero)
