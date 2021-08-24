#ejercicio1
for n in range(10):
  print(n)

#ejercicio2
for n in range(100,200):
  print(n)

#ejercicio3
for n in range(5,20,3):
  print(n)

#ejercicio4
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)

#ejercicio5
c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
   numero=int(input("Número: "))
   total+=numero
print("Total de la suma:", total)

#ejercicio6
frase=input("Frase: ")
print("Vocales en la frase:")
for m in "aeiou":
  if m in frase:
    print(m)

#ejercicio7
total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total)

#ejercicio8
anioInicio=int(input("Año inicial:"))
anioFin=int(input("Año final:"))
for anio in range(anioInicio, anioFin+1):
   if not anio%10==0:
       continue
   if not anio%4==0:
       continue
   if anio%100!=0 or anio%400==0:
       print(anio)

#ejercicio9
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

#ejercicio10
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3