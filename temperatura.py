temperatura=float(input("ingrese la temperatura actual:"))
menufrio=["ensalada", "arroz"]
menucaliente=["sopa", "guiso"]
if temperatura>=25:
    print("el menu sugerido para este tiempo de calor es:", menufrio)
else:
    print("el menu sugerido para este tiempo de frio es:", menucaliente)