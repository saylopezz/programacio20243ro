lados= int(input("ingresar la cantidad de lados"))
if lados==4:
    l1=int(input("ingrese el valor del primer lado:"))
    l2=int(input("ingrese el valor del segundo lado:"))
    l3=int(input("ingrese el valor del tercer lado:"))
    l4=int(input("ingrese el valor del cuarto lado:"))

    if l1==l2 and l1==l3 and l1==l4:
        print("la figura podra ser un cuadrado o rombo")
    else:
        print("la figura podra ser un rectangulo o un paralelogramo")
elif lados==3:
    print("la figura geometrica es un triangulo")
