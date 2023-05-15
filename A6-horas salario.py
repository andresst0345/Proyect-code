print("puta generacion de tiktokers dame tu informacion que tambien roba facebook")

sl = float (input("ingrese el valor por hora cotizada=="))
hr = float (input("ingrese las horas trabajadas = "))
im = float(input("ingresa el porentaje de impuestos que quita petro  ="))

sueldo = (sl*hr)
op = (sueldo / 100) *im
neto = sueldo - op 

print("el sueldo neto es ==>",neto)
