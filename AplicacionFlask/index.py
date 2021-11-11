from re import A
import numpy as np
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from os import remove
'''
import math 
from matplotlib import pyplot as plt
import shutil
'''
import shutil
import string
import random


app = Flask(__name__)

"""
@app.route('/')
def principal():
    # return "Bienvenido o bienvenida a mi sitio web con python!"
    return "UskoKruM2010 - Suscríbete!"
@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"
"""
c = 10
r = 10

@app.route('/')
def principal():
    return render_template('lenguajes.html')

@app.route('/lenguajes', methods=['POST', 'GET'])
def lenguajes():
  num = 1
  cuantas = 2
  rt = 2
  palabra="a" 
  palabra2="b"
  cont=1

  if request.method == "POST":
    cuantas = request.form['cuantas']
    rt = request.form['rt']
  rt = int(rt)
  cuantas =int(cuantas)
  #variabes globales
  global c
  global r
  c=cuantas
  r=rt
  print(c)
  while num<cuantas:
    palabra=palabra+"a"
    num=num+1
  num=1
  while num<rt:
    palabra2=palabra2+"a"
    num=num+1

  misLenguajes=palabra
  misLenguajes2=palabra2

  return render_template('contatco.html', lenguajes=misLenguajes, lenguajes2=misLenguajes2, contador=cont)

@app.route('/contacto', methods=['POST', 'GET'])
def contacto():
  vector = {}
  vector2 = {}
  vector3 = {}
  vector4 = {}
  i=0

  if request.method == "POST":
    objetivo = request.form['objetivo']

    while i<c:
      a=i+1
      a = str(a)
      x1 = request.form['x'+a]
      vector[i] = float(x1)
      i=i+1

    i=0
    j=0
    cont=0
    while j<r:
      i=0
      while i<c:
        a=i+1
        a = str(a)
        b=j+1
        b = str(b)
        x1 = request.form['y'+b+a]
        vector2[cont] = float(x1)
        i=i+1
        cont=cont+1
      j=j+1
    
    i=0
    while i<r:
      a=i+1
      a = str(a)
      x1 = request.form['z'+a]
      vector3[i] = float(x1)
      bi = request.form['r2'+a]
      vector4[i] = str(bi)
      i=i+1

          
  for v in vector:
      print(v)

  print(objetivo)

  print("HOLA")
  print(vector[1])
  for v2 in vector2:
      print(v2)
  
  
  print("Vecotor3")
  for v3 in vector3:
      print(v3)

  print("Vecotor4")
  for v4 in vector4:
      print(v4)

  if c==2:
    i=0
    cont=0
    x = np.arange(-10, 15, 5)
    y = np.arange(-10, 15, 5)
    colors=['b','g','r','y','k','p']
    while i<(c*r):
      y1=((vector3[cont]) - (vector2[i]*x))/(vector2[i+1])
      plt.plot(x, y1, linewidth=2, color=colors[cont],label='RT')
      i=i+2
      cont=cont+1

    length=3  
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.grid()
    plt.title('Método Gráfico')
    plt.savefig("grafica.jpg")
    shutil.copy("grafica.jpg", "static/grafica.jpg")
    plt.clf()


  '''
  x=np.array(range(20))*-1
  y = np.zeros(len(x))
  for i in range(len(x)):
    y[i] = math.sin(x[i])
  y=np.array(range(20))*2
  plt.plot(x,y)
  plt.title("grafica")
  plt.savefig("grafica.jpg")
  shutil.copy("grafica.jpg", "static/grafica.jpg")
  ''' 

  matrizIngresada, matrices, matrices2, tamaño, tamaño2, mensaje, Rz, result, tam = programa(objetivo, vector, vector2, vector3, vector4)
  print("AQUI VAMOS EXCELENTE")
  for e in result:
      print(e)
  return render_template('resultado.html', matriz=matrizIngresada, m1=matrices, m2=matrices2, t1=tamaño, t2=tamaño2, imp=mensaje, Rez=Rz, resultT=result, tresultado=tam, desplegar="Problema con Múltiples Soluciones", cabeza=vector, g=c)

#Calcular Zj-Cj : CB · Aj - Cxj , ∀j = 1,...,n.
def puntomenos(A,ren,col):
  i = 1
  while i < col:
    z = np.dot(A[1:ren-1,0],A[1:ren-1,i]) - A[0,i] #Cálculo de producto punto
    A[ren-1,i] = z                                 #por medio de np.dot.
    i+=1
  print (A)   #Impresión de las iteraciones como matrices.
  print ( )
  return (A)  #Regresa la matriz con producto punto.

#Busca el valor pivote entre las filas y columnas
def pivote(A,ren,col):
  i = 1
  min1= np.amin(A[ren-1,1:col-1])         #Buscar el Zj-Cj mínimo de los Zj-Cj < 0
  mincol = np.argmin(A[ren-1,1:col-1]) +1 #para que sea la columna pivote.
  E = A[1:ren-1,mincol]
  posi2 = E[E>0]
  if posi2.size == 0:
    print("Problema no acotado")
    return(-1,-1,-1)
  min2 = 100000000000
  while i < (ren-1):
    if (A[i,mincol] !=0):
      z = A[i,col-1] / A[i,mincol]  #Dividir cada elemento d con su respectio en
      if i == 1 and z >=0:         #columna pivote, para obtener d^.
        min2 = z
        minreg = i
      elif z < min2 and z >=0:
        min2 = z
        minreg = i    #Seleccionar el renglón que contenga el elemento en d^ con el
    i+=1            # menor valor de los d^ positivos, para ser renglón pivote.          

  piv = A[minreg, mincol] #Se encontraron renglón y columna pivote.
  #print (min2)
  #print(minreg, mincol)
  return (piv, minreg, mincol)

#Actualizar tabla
def nuevatabla(A, pivreg, pivcol, piv, ren, col):
  A [pivreg, 0] = A [0, pivcol]
  i = 1
  while i < col:
    #print(A [pivreg,i] , A[pivreg,i], piv)
    if (piv !=0 ):
      A [pivreg,i] = A[pivreg,i] / piv #Nuevo renglón piv = elemnto en ren. anterior
                                       #entre valor pivote misma columna.
    i+=1
  i = 1
  j = 1
  while i < (ren -1):
    if i != pivreg:
      j=1
      nuepiv = A[i,pivcol]
      while j < col:
        #print(A[i,j], nuepiv, A[pivreg,j])
        A[i,j] = A [i,j] - (nuepiv*A[pivreg,j]) #elem.ren = elem.renglón anterior 
        j+=1                                    #en misma columna - (elem en renglón
                                                #anterior en la columna pivote * elem
                                                #en nuevo renglón pivote en misma columna)
    i+= 1
  #print(A)
  return (A)

#Impresión de los resultados
def numequis2 (A, num_var,ren,col,obj):
  result= {}
  tam="a"
  Rz=0
  if (A[ren-1,col-1] == 0):
    mensaje ="La matriz introducida no tiene solución con este programa Simplex"
    print(mensaje)
  else:
    j = 1
    quita = ren - 2
    while (j< col- quita - 1): 
      i = 1
      ban = 0
      while (i<ren-1):
        if(A[i,0]==A[0,j]):
          print('x'+str(j)+' = ',(A[i,col-1])) #Buscar los resultados de x y z dentro
          tam=tam+"a"
          result[j] = A[i,col-1]
          ban = 1                              #de la matriz.
        i+=1
      if (ban == 0):
        print('x'+str(j)+' =  0.0')
        tam=tam+"a"
        result[j] = 0
      j+=1
    if obj == "min":
      A[ren-1,col-1] = A[ren-1,col-1] * -1
    print("z  = ",A[ren-1,col-1])
    Rz = A[ren-1,col-1]
    if (np.count_nonzero(A[ren-1, num_var:])!=(col-1-num_var)):
      mensaje = "Problema con Múltiples Soluciones"
      print(mensaje+"\n")
      print("")
    else:
      mensaje = "Solución óptima"
      print(mensaje)
  return (mensaje, Rz, result, tam)

def fases (A, ren, col, num_var,ban):
  ite = 0
  matrices = {}
  tamaño = "a"
  mensaje = "NO):"
  while ban>=1:
    print("Iteracion: ",ite)
    A = puntomenos(A, ren,col)
    matrices[ite] = np.copy(A)
    tamaño=tamaño+"a"
    B = A[ren-1,:]
    C = A[ren-1,:col-2]
    negat = B[B<0]
    negat2 = C[C<0]
    if negat.size == 0 and ban == 1: # ¿Todos los Zj-Cj >= 0?
      ban = 0 #Sí
    elif negat.size == 1 and ban == 2 and A[ren-1,col-1] < 0:
      ban = 0 #Sí
    elif negat.size == 0 and ban == 2:
      ban = 0 #Sí
    else: #No
      if negat2.size == 0 and ban == 1:
        mensaje = "Problema no factible"
        print("Problema no factible")
        ban = -2
      else:
        piv, pivreg, pivcol = pivote(A,ren,col)
        if(pivreg == -1 and pivcol == -1 and piv == -1):
          mensaje = "Problema no acotado"
          ban = -1
        else:
          A = nuevatabla(A,pivreg,pivcol,piv,ren,col)
    ite +=1
  ite = 1
  return (A,ban,matrices,tamaño,mensaje)

def balanceo (A,ren,col):
  i=1
  while i< col:
    cons = 0
    j = 1
    while j < ren:
      if (A[j,i] == 0 or A [j,i] == 1):
        if A[j,i] == 1 and cons ==0:
          cons = j
        elif A[j,i] == 1 and cons > 0:
          cons = -1
      else:
        cons= -1
      j +=1
    if (cons > 0):
      A[cons,0] = A[0,i]
    i += 1
  return (A)

def pedir_datos(objetivo, vector, vector2, vector3, vector4):
  num_var = c
  num_res = r
  num_art = 0
  num_exc = 0
  print("ENTRAMOS BIEN")
  print(c)
  print(r)
  i = 0
  tipo1 = objetivo
  print("MANDAMOS BIEN")
  print(tipo1)
  print("Coeficientes de la función:\n")
  Coeficientes = np.array([[0]],dtype='f')
  while i<num_var:
    x = (float)(vector[i])
    if(tipo1 == "min"):
      x *= (-1)
    Coeficientes = np.append(Coeficientes, x)
    i += 1
  Coeficientes = np.append(Coeficientes, 0)
  Tabla = np.zeros((num_res+2,num_var+2))
  i = 0
  aux=0
  while i < num_res:
    print("Restricción"+str(i+1)+"\n")
    j = 0
    renglon, columna = Tabla.shape
    while j < num_var:
      x = (float)(vector2[aux])
      Tabla[i+1,j+1] = x
      j += 1
      aux += 1
    x = (float)(vector3[i])
    Tabla[i+1,columna-1] = x
    tipo = vector4[i]
    if Tabla[i+1,columna-1] < 0:
      Tabla[i+1,:] = np.negative(Tabla[i+1,:])
      if tipo == "ma":
        tipo = "me"
      elif tipo == "me":
        tipo = "ma"
    if tipo == "ma":
      columna = np.zeros((num_res+2))
      columna[i+1] = -1
      columna1 = np.zeros((num_res+2))
      columna1[0] = -1
      columna1[i+1] = 1
      Tabla = np.insert(Tabla, num_var+ 1 + num_exc ,columna, axis = 1)
      num_art +=1
      Tabla = np.insert(Tabla, num_var+ 1 + num_exc + num_art ,columna1, axis = 1)
      num_exc +=1
    elif tipo == "ig":
      columna1 = np.zeros((num_res+2))
      columna1[0] = -1
      columna1[i+1] = 1
      Tabla = np.insert(Tabla, num_var+ 1 + num_exc + num_art ,columna1, axis = 1)
      num_art +=1
    elif tipo == "me":
      columna = np.zeros((num_res+2))
      columna[i+1] = 1
      Tabla = np.insert(Tabla, num_var+ 1 + num_exc ,columna, axis = 1)
      num_exc +=1
    i += 1
    #print(Tabla)
  i = 0
  while i < num_exc:
    Coeficientes = np.append(Coeficientes, 0)
    #columna = Coeficientes.shape
    #Coeficientes = np.insert(Coeficientes, columna, 0)
    i += 1
  return (Tabla, Coeficientes, num_art, num_var, tipo1)
    
def programa(objetivo, vector, vector2, vector3, vector4):
    result = {}
    tam="a"
    Rz=0   
    mensaje="Hola"
    A, Coe,num_art, num_var, obj = pedir_datos(objetivo, vector, vector2, vector3, vector4)

    print("Matriz ingresada:\n",A)
    #print(Coe)

    matrizIngresada = np.copy(A)
    ren , col = A.shape

    A = balanceo(A, ren, col)

    
    

    print("---FASE I---\n")
    A, ban, matrices, tamaño, mensaje = fases (A, ren, col,num_var,1)
    if num_art > 0:
      A = np.delete(A , np.s_[col-num_art-1:col-1], 1)
    A[0] = Coe
    ren , col = A.shape
    A = balanceo(A, ren, col)

    if ban==-2:
      matrices2=matrices
      tamaño2=0

  
    if  ban == 0:
      print("\n---FASE II---\n")
      A,ban, matrices2, tamaño2, mensaje = fases (A, ren, col,num_var,2)
    if ban == 0:
      print("Resultado:")
      mensaje, Rz, result, tam = numequis2(A,num_var,ren,col,obj)
    
    
    return (matrizIngresada, matrices, matrices2, tamaño, tamaño2, mensaje, Rz, result, tam)

if __name__ == '__main__':
    app.run(debug=True)
