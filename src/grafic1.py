#! encoding: UTF-8
import matplotlib.pyplot as pl
import time
import timeit
import modulo

y=[]
e=[]
m=[]
def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)
if __name__=="__main__":
   import sys
   if (len(sys.argv)==4):
     p1=int(sys.argv[1])
     p2=int(sys.argv[2])
     p3=float(sys.argv[3])
   else:
     print "Usted debe proporcionar tres valores, errorpi.py y tres valores numéricos, ahora se ejecutará por defecto con los valores 5 5 0.1"
     p1=5
     p2=5
     p3=0.1
     
   f=open("tiempo y errores", 'w')
   #print "Introduzca el nombre del fichero para almacenar los resultados:"
   #nombre_fichero= raw_input();
   
   for i in range (1,5):
    p1=p1*i
    p3=p3*i
    start=time.time()
    s=error(p1,p2,p3)
    finish=time.time()-start
    print "El porcentaje de error es de: %5.3f" %s
    print "El tiempo que tarda en realizarse es: %14.13f" %finish
    y=y+[finish]
    e=e+[p1]
    m=m+[p3]
    f.write(str(finish) + '\n')
    f.write(str(s) + '\n')
   f.close()
   
   print y
   x = [1,2,3,4]
   graf1=pl.subplot(211)
   pl.plot(x,y, 'r--')
   pl.xlabel("Intervalos")
   pl.ylabel("Tiempo")
 
   graf2= pl.subplot(212)
   pl.plot(e,m, 'r--')
   pl.xlabel("Error")
   pl.ylabel("Umbral")
   pl.savefig("Graficas.eps", dpi=100)
   pl.show()
   
   

