"""Ximena Hernández
fecha : 21 de sep del 2023"""
print("Ximena Alejandra Hernández Gómez")

x = input("Escriba un número en el rango de 1 a 10 ")
xnum = int(x)

if xnum < 1 or xnum > 10:
    print("El número que ingreso se encuentra fuera del rango solicitado")

for i in range(0, 10):
    print(xnum, "x", (i+1), "=", xnum*(i+1))
          
opcion = input("Escriba 'continuar' si desea generar la tabla de otro número o 'cerrar' para salir del programa " )

while opcion == "continuar":
    x = input("Escriba un número en el rango de 1 a 10 ")
    xnum = int(x)

    if xnum < 1 or xnum > 10:
        print("El número que ingreso se encuentra fuera del rango solicitado")

    for i in range(0, 10):
        print(xnum, "x", (i+1), "=", xnum*(i+1))
    opcion = input("Escriba 'continuar' si desea generar la tabla de otro número o 'cerrar' para salir del programa " )
else:
    print("de nada, vuelva pronto")
