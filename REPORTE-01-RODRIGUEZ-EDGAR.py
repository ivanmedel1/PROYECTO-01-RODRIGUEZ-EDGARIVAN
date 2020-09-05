#PROGRAMA DE INFORME DE LA TIENDA LIFESTORE
#AUTOR=EDGAR IVAN RODRIGUEZ MEDEL
#Contacto:ivan.rodmed98@gmail.com.
#Telefono: 9331335091

from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products


################################ Calculando las listas necesarias para el informe

#LISTAS NECESARIAS PARA VENTAS


total1=[] #Listas para guardar los resultados de contar las ventas
total2=[]

for prod in lifestore_products:     #Iniciamos un ciclo for para recorrer todos los id de la lista de productos
  contador=0                        #Reiniciamos el contador de las ventas a cero
  for comparar in lifestore_sales:  #Hacemos un for dentro del primero para recorrer las ventas
    if prod[0]==comparar[1]:        #Si (if) el id de la lista productos es igual entonces lo agrega a contador
      contador+=1
    else:
      continue                      #Si no para esto entonces continua con el siguiente venta
  
  total1.append([prod[0],contador,prod[4]])       #Cuando termine de recorrer todas las ventas guarda en las listas
  total2.append([prod[0],contador,prod[4]])       #el [Id, total de ventas del producto, el stock]

#Generando una lista con las ventas de mayor a menor
venta_mayor=[]                     #Hacemos una lista vacia para guardar ahí la ventas ordenadas de mayor a menor
while total1:                      #Empezamos ciclo while que va a recorrer los valores de de las ventas
  maximo= total1[0][1]             #Suponemos que el valor máximo es el primer valor
  lista= total1[0]                 #Suponemos que la lista del primer valor es el valor máximo
  for ventas in total1:            #Recorremos la lista total1
    if ventas[1] > maximo:         #Si encontramos un valor mayor al que supusimos que era el máximo entonces:
      maximo=ventas[1]             #Ese valor será el nuevo máximo
      lista=ventas                 #Esa lista será la nueva máxima
  venta_mayor.append(lista)        #Cuando termine entonces agregará el valor máximo a la lista venta_mayor
  total1.remove(lista)             #Removemos el valor de la lista total1 y se reinicia hasta que total1 no tenga nada


#generando una lista con las ventas de menor a mayor
venta_menor=[]                    #Para esta lista es la misma que la lógica anterior con el cambio de que se invierte
while total2:                     #el signo de la condición para ahora tomar los valores mínimos
  minimo= total2[0][1]            
  lista= total2[0]
  for ventas in total2:
    if ventas[1] < minimo:
      minimo=ventas[1]
      lista=ventas
  venta_menor.append(lista)
  total2.remove(lista)           #Tenemos que usar la lista total2 porque la otra ya la habíamos vaciado.

#LISTAS NECESARIAS PARA BUSQUEDA

id_product = 0                   #La analogía es la misma que la de ventas aunque ahora se usa la lista busqueda
totalbusqueda1=[]
totalbusqueda2=[]

for prod in lifestore_products:
  contador=0
  for comparar in lifestore_searches: #Uso de la lista busqueda y si encuentra el id entonces lo agrega al contador
    if prod[0]==comparar[1]:
      contador+=1
    else:
      continue
  
  totalbusqueda1.append([prod[0],contador,prod[4]])
  totalbusqueda2.append([prod[0],contador,prod[4]])

#print(totalbusqueda1)

#generando una lista con las busqueda de mayor a menor
busqueda_mayor=[]                     #La analogía es la misma que la explicada en la de ventas de mayor a menor.
while totalbusqueda1:
  maximo= totalbusqueda1[0][1]
  lista= totalbusqueda1[0]
  for busqueda in totalbusqueda1:
    if busqueda[1] > maximo:
      maximo=busqueda[1]
      lista=busqueda
  busqueda_mayor.append(lista)
  totalbusqueda1.remove(lista)

#generando una lista con las busqueda de menor a mayor
busqueda_menor=[]                     #La analogía es la misma que la explicada en la de ventas de mayor a menor.
while totalbusqueda2:                 #solo que ahora se usa para las busquedas y cambia el signo para que busque el
  minimo= totalbusqueda2[0][1]        #valor menor
  lista= totalbusqueda2[0]
  for busqueda in totalbusqueda2:
    if busqueda[1] < minimo:
      minimo=busqueda[1]
      lista=busqueda
  busqueda_menor.append(lista)
  totalbusqueda2.remove(lista)


#LISTAS NECESARIAS PARA RESEÑA.

Lista_reseña=[]                      #Creamos la lista para guardar la reseña.
total_reseña1=[]
total_reseña2=[]

for prod in lifestore_products:     #Iniciamos el ciclo for para recorrer los id de los productos.
  contador=0
  suma_estrellas=0                  #Generamos una variable =0 que sume el score del producto.
  reseña=0                          #Generamos una variable para guardar ahí el calculo de la reseña promedio.
  for comparar in lifestore_sales:  #Iniciamos un ciclo for para recorrer las ventas.
    if prod[0]==comparar[1]:        #Si (if) los id se parecen entonces:
      contador+=1                   #Sumamos al contador para registrar que hubo una venta con ese id.
      suma_estrellas+=comparar[2]   #Sumamos el score que tuvo esa venta que se encuentra en comparar[2] a la variable.
    else:
      continue                      #Si no coincide el id entonces continua.
  if contador != 0:                 #Antes de calcular la media aritmética debemos saber si el contador es diferente de
    reseña=suma_estrellas/contador  #cero para no generar error en la división, si cumple hace la media arimética.
    total_reseña1.append([prod[0],contador,reseña,prod[4]]) #Agregamos: [id,ventas,media de reseñas,stock]
    total_reseña2.append([prod[0],contador,reseña,prod[4]]) 

#total_reseña=[id producto, total ventas, media de reseña]

#generando una lista con las reseñas de mayor a menor
reseña_mayor=[]                     #La analogía es la misma que la explicada en la de ventas de mayor a menor.
while total_reseña1:                #Ahora queremos ordenar las reseñas, es por eso que comparamos con estas
  maximo= total_reseña1[0][2]
  lista= total_reseña1[0]
  for rese in total_reseña1:
    if rese[2] > maximo:
      maximo=rese[2]
      lista=rese
  reseña_mayor.append(lista)
  total_reseña1.remove(lista)

#print(reseña_mayor)

#generando una lista con las reseñas de menor a mayor
reseña_menor=[]                     #La analogía es la misma que la explicada en la de ventas de mayor a menor.
while total_reseña2:                #Cambiando el signo de menor a mayor
  minimo= total_reseña2[0][2]
  lista= total_reseña2[0]
  for rese in total_reseña2:
    if rese[2] < minimo:
      minimo=rese[2]
      lista=rese
  reseña_menor.append(lista)
  total_reseña2.remove(lista)

#Lista de categorias
categorias=[]                  #Debido a que nos piden las ventas y busquedas por categoria haremos una lista con las categorias
norepcategoria= 'nada'            #Generamos una variable que tenga una cadena de caracteres que no coincida con la primera categoria encontrada
for categoria in lifestore_products:    #iniciamos ciclo for para acanzar producto por producto y ver su categoria
  if norepcategoria == categoria[3]:    #Si la categoria del producto es igual a la guardada en norepcategoria entonces salta el producto
    continue
  else:
    categorias.append(categoria[3])     #Si no es el mismo entonces la guarda en la lista categorias
    norepcategoria=categoria[3]         #Ahora la nueva no repcategoria es la categoria que no se repitió 

##############################################

Lista_admin=[['Edgar','123'],['Ivan','123'],['a','a']] #Lista de los usuarios admitidos

#INICIAMOS MENU DE INGRESO
opcion= '1'                 #Hacemos una variable opcion=1 para activar el while siguiente
while opcion=='1':          #Este while es el general, mientras opcion=1 no cambie de caracter entonces se seguirá repitiendo.
  usuario=input('Ingresa tu nombre de usuario \n (Recuerda las mayusculas y minusculas y sin acentos): ') #Ingreso de usuario
  pin=input('Ingresa tu contraseña: ') #Ingreso de contraseña
  for verificar in Lista_admin:        #Se abre ciclo for para recorrer la lista de admin permitidos

     if verificar[0]==usuario and verificar[1]==pin: #Si el usuario y la contraseña es correcta entonces:
          print(' ')
          print('Bienvenido '+ usuario)              #Imprime el bienvenido y nombre de usuario
          print(' ')
          opcion=2           #cambia la opción a 2 para que la condicion del while de ingreso no se siga cumpliendo y termine.
          administrador='1'  #Nombre la variable administrado=1 para activar el siguiente while que será el del menú.
          break              #Rompe el cicl actual.
     else:                                        #Si no lo cumple y además es el último valor de la lista admin entonces:
        if verificar[0]==Lista_admin[-1][0]:      #If para verificar si es el último valor de la lista.
          print('No se ha encontrado el usuario o contraseña incorrecta')   #Hace saber al usuario que algo es incorrecto.
          opcion=input('¿Desea reintentarlo? (si=1/no=cualquier tecla):')   #si el usuario pide que se vuelva a intentar tiene que ingresa 1 para que opcion se siga cumpliento y se siga repitiendo el while del login, si pone otra letra simplemente cambia el valor de opcion significando que corta el while del menu ingreso.
          administrador='no cumpla con el while administrador' #Además nombreamos la variable administrador otra cadena para que no cumpla con el while del menu principal y no se active.
          break #Corta el ciclo actual.

################################################

#MENU PRINCIPAL
while administrador=='1':   #Si ingresamos correctamente entonces se activa el ciclo while principal
  menu=input('MENU ADMINISTRADOR \n Elija una categoría \n 1.-Ventas y busqueda de productos \n 2.-Reseñas de productos \n 3.-Ingresos y total de ventas \n 4.Consultar un id \n 5.-Salir \n Elija un NÚMERO: ')  #El usuario decide que categoría quiere ver.
  print('  ')
  if menu=='1':                       #Si elije 1 entonces hace a la variable menu=1 para activar ciclo while de esta categoria.
    print('1.-Ventas y busqueda de productos')

  elif menu=='2':                     #Si elije 2 entonces hace a la variable menu=2 para activar ciclo while de esta categoria.
    print('2.-Reseñas de productos')

  elif menu=='3':                     #Si elije 3 entonces hace a la variable menu=3 para activar ciclo while de esta categoria.
    print('3.-Ingresos y total de ventas')
  
  elif menu=='4':                     #Si elije 4 entonces hace a la variable menu=4 para activar el while que consulta id.
    print('4.-Consulta de id')

  elif menu=='5':                     #Si elije 5 entonces imprime el agradecimiento y se sale.
    print('Gracias por utilizar el servicio')
    break
  else:                               #Si el usuario no elije ninguna de las opciones anteriores vuelve a preguntar que si desea intentarlo de nuevo (si oprime 1 entonces el ciclo while del menu principal se sigue cumpliendo y reinicia, si oprime otra tecla entonces deja de cumplir el ciclo while y termina el programa porque deja de cumplirse otro ciclo while de abajo)
    print('No se ha elejido un número correcto') 
    administrador=input('¿Desea reintentarlo? (si=1/no=cualquier tecla para salir):') 

#--------------------------#
#VENTAS Y BUSQUEDAS
  while menu=='1':          #Si el usuario eligió 1 en el menú principal entonces se activa este while.
    menup1= input('Elija una opción: \n 1.-Ventas \n 2.-Busquedas \n 3.-Regresar \n Elige un NÚMERO: ') #Dentro hay otro menu que activará los while que están dentro de esta categoria.
    print('  ')
    if menup1=='1':         #Si se elije  1 entonces activará la subcategoria ventas (por while menup1=1)
      print('VENTAS')
    elif menup1=='2':       #Si se elije 2 entonces se activará la subcategoria busqueda (por while menup1=2)
      print('BUSQUEDAS')    
    elif menup1=='3':       #Si se elije 3 entonces: no se activan las subcategorias (porque menup1 no obtiene ningun valor) 
      (' ')
      administrador=='1'    #Le da el valor =1 para mantener el bucle del menu principal funcionando
      menu='romper bucle while menu 1'  #Le asignamos otro valor a menu para que deje de cumplir el while de la categoria 'ventas y busquedas'
    else:                   #Si no elije ninguna de las anteriores entonces:
      print('No se ha elejido un número correcto')
      menu=input('¿Desea reintentarlo? (si=1/no=cualquier tecla para salir):')  #Le pregunta si quiere reintentarlo.
      print('  ')
      if menu!='1':   #Si no le da el valor 1 a menu entonces se rompe el while de la cateogoria 'ventas y busquedas'.
        administrador='para romper el blucle principal' #Rompe el ciclo principal al darle otro valor a 'administrador'.
    
       #SUBCATEGORIA: VENTAS
    while menup1=='1': #Si el usuario eligió esta 1 en menup1 entonces se activa esta subcategoria.
      print('El top 20 de las mejores ventas es:')
      topventas20=venta_mayor[0:19]     #guardamos en una lista los primeros 20 valores de la lista venta_mayor ya calculado en el principio.
      for impr in topventas20:  #imprimimos los mejores productos y sus mejores ventas [id,venta,stock disponible]
        print('El id: ', impr[0],'tiene: ', impr[1], 'ventas y',impr[2],'stock' )
      print('Nota: Si desea ver las especificaciones de un id regrese al menú principal')
      decision_categoria=input('Desea ver la info de ventas por categoria (si=1/no=cualquier tecla para regresar al menú princial): ')     #Preguntamos al usuario si desea ver las ventas por categorias ordenadas de mayor a menor, si así lo quiere entonces se activa el while decision_categoria, si no es así entonces regresamos al menú principal.
      while decision_categoria=='1':
        #Menu donde le vamos a pedir al usuario qué categoría quiere ver:

        opcioncat=input('¿Qué categoria quiere ver info de ventas?: \n 1. procesadores \n 2. tarjetas de video \n 3. tarjetas madre \n 4. discos duros        \n 5. memorias usb \n 6. pantallas \n 7. bocinas \n 8. audifonos \n seleciona un NÚMERO: ') #El usuario desea que categoria ver:
        if opcioncat=='1': #Si elije la categoria 1, por ejemplo entonces de la lista que contiene las categoria le va a asignar ese valor a opcioncat.
          opcioncat=categorias[0]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='2':
          opcioncat=categorias[1]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='3':
          opcioncat=categorias[2]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='4':
          opcioncat=categorias[3]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='5':
          opcioncat=categorias[4]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='6':
          opcioncat=categorias[5]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='7':
          opcioncat=categorias[6]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        elif opcioncat=='8':
          opcioncat=categorias[7]
          print('Las ventas de', opcioncat, 'ordenadas de menores ventas a mayores ventas son:')
        else:     #Si no elije una correcta entonces imprime que no se eligió una opcion correca.
          print('No elejiste una opción valida, vuelve a intentarlo')
        
        #Iniciando bucle para extraer de la lista de productos solo aquellos que coincidan en categoria.
        lista_categoria=[]   #Creamos lista vacia para ingresar ahí los productos de la categoria
        for lista in lifestore_products: #Recorremos en un ciclo for todos los productos de la lista.
          if lista[3]==opcioncat:        #si la categoria del producto coincide con la categoria que elegimos en la entrada anterior entonces:
           lista_categoria.append(lista) #Agrega el producto a la lista_categoria.
          else:
            continue    #Si no es así lo salta y continua con el siguiente.


        #Imprimiendo las ventas de menor a mayor de la categoria elegida.
        for menor in venta_menor:          #ciclo for para recorrer cada valor de la lista de ventas ordenadas de menor a mayor.
          for producto in lista_categoria: #Segundo for para recorrer los productos de la categoria elegida
            if menor[0] == producto[0]: #si el id del producto de la lista venta_menor es igual al id del producto de la categoria elegida entonces:
              for busqueda in busqueda_menor: #Se abre un tercer ciclo for para buscar las busquedas totales del producto.
                if busqueda[0]== menor[0]: #Si se cumple entonces imprime[id del producto de la categoria, ventas, busqueda, stock]
                  print('El id:', menor[0], ' ha tenido:', menor[1],  ' ventas,', busqueda[1], 'busquedas y',menor[2],'stock')
                  continue
              else:
                continue #Estos else son para que cuando no cumpla con algun if anterior lo salte y siga con el siguiente valor
            else:
              continue
        #Imprimiento pregunta al usuario para saber si desea volver a consultar otra categoria
        decision_volver=input('¿Desea consular otra categoria? (si=1/no=cualquier tecla para regresar al menu principal): ')
        if decision_volver=='1': #Si su decisión es sí entonces no cambia nada del ciclo while y por lo tanto se regresa a la linea 231 que corresponde a while 'decision_categoria=='1'
          continue
        else: #Si no es así rompe las tres categorias para regresar hasta la linea 181 que corresponde al while del menu principal.
          decision_categoria='romper bucle categoria'
          menup1='Romper el buble de las ventas'
          menu='romper bucle while menu 1'
      
      else: #Si el usuario no elije ninguna categoria entonces regresa al menu principal (linea 181)
        menup1='Romper el buble de las ventas'
        menu='romper bucle while menu 1'
        administrador='1'

    #SUBCATEGORIA: BUSQUEDAS
    while menup1=='2':          #Si el usuario eligió esta 1 en menup1 entonces se activa esta subcategoria.
      print('Busquedas')        #Hacemos saber al usuario que está en busquedas
      print('El top 40 de los productos más buscados son:') 
      topbusqueda40=busqueda_mayor[0:39] #En una lista nueva guardamos los primero 40 valores de la lista busquedas_mayor que ordena las busquedas de mayor a menor
      for impr in topbusqueda40:  #Impresión de la lista de busqueda
        print('El id: ', impr[0],'tiene ', impr[1], 'busquedas y',impr[2],'stock' ) #[id,busqueda, stock]

      print('  ')  
      decision_categoria=input('¿Desea ver la info de busquedas por categoria? (si=1/no=cualquier tecla para regresar al menú princial): ') #Preguntamos al usuario si quiere ver por categoria.
      #si elije que si entonces se activa el siguiente while
      while decision_categoria=='1': #Menu donde le vamos a pedir al usuario qué categoría quiere ver 

        opcioncat=input('¿Qué categoria quiere ver info de busquedas?: \n 1. procesadores \n 2. tarjetas de video \n 3. tarjetas madre \n 4. discos duros        \n 5. memorias usb \n 6. pantallas \n 7. bocinas \n 8. audifonos \n seleciona un NÚMERO: ')
        if opcioncat=='1': #La metodologia es la misma explicada que en la subcategiria ventas.
          opcioncat=categorias[0]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='2':
          opcioncat=categorias[1]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='3':
          opcioncat=categorias[2]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='4':
          opcioncat=categorias[3]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='5':
          opcioncat=categorias[4]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='6':
          opcioncat=categorias[5]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='7':
          opcioncat=categorias[6]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        elif opcioncat=='8':
          opcioncat=categorias[7]
          print('Las busquedas de', opcioncat,   'ordenadas de menor a mayor son:')
        else:
          print('No elejiste una opción valida, vuelve a intentarlo')

        #Iniciando bucle para extraer de la lista de productos solo aquellos que coincidan en categoria.
        lista_categoria=[]  #Creamos lista vacia para ingresar ahí los productos de la categoria
        for lista in lifestore_products:
          if lista[3]==opcioncat:
           lista_categoria.append(lista)
          else:
            continue
        #imprimiendo la busqueda de menor a mayor
        for menor in busqueda_menor:
          for producto in lista_categoria:  #primer for para imprimir el producto
            if menor[0] == producto[0]: #si la categoria del producto coincide con la categoria que elegimos en la entrada anterior entonces:
              for busqueda in venta_menor:   #segundo for para imprimir las ventas 
                if busqueda[0]== menor[0]: #buscamos las ventas que coincidan con busqueda
                  print('El id:', menor[0], ' ha  tenido:', menor[1],  ' busquedas y  ',busqueda[1], 'ventas y',menor[2],'stock')
                  continue #impresión de busqueda por categoria[id,busqueda,venta,stock]
              else:
                continue
            else:
              continue

        decision_volver=input('¿Desea consular otra categoria? (si=1/no=cualquier tecla para regresar al menu principal): ') #Preguntamos al usuario si quiere ver por categoria.
      #si elije que si entonces se activa el siguiente while
        if decision_volver=='1': #Si decide que si entonces no cambia ningun valor por lo que regresa al while decision_categoria=='1' de la linea 308
          continue
        else: #Si no es así rompre lo ciclos de la busqueda por categoria, subcategoria y categoria, regresando al menu principal
          decision_categoria='romper bucle categoria'
          menup1='Romper el buble de las ventas'
          menu='romper bucle while menu 1'
      
      else: #Si el usuario no elije ninguna categoria entonces regresa al menu principal rompiendo los ciclos de la busqueda, categoria. (linea 181)
        menup1='Romper el buble de las busqueda'
        menu='romper bucle while menu 1'
        administrador='1'
#--------------------------#

#--------------------------#
#EMPIEZA LA CATEGORIA RESEÑAS DE PRODUCTOS
  while menu=='2':         #Si el usuario eligió 2 en el menú principal entonces se activa este while.
    print('Los 20 productos con mejores reseñas son') 
    reseña_mayor20=reseña_mayor[0:19] #Se hace una lista que tome solo los primeros 20 valores de la lista de reseñas de mayor a menor.
    for impr in reseña_mayor20:
     print('El id: ', impr[0],'tiene una reseña de: ', "{:.2f}".format(impr[2]) ) #Impresión [id,reseña media aritmética]

    print('Los 20 productos con las peores reseñas')
    reseña_menor20=reseña_menor[0:19] #Se hace una lista que tome solo los primeros 20 valores de la lista de reseñas de menor a mayor.
    for impr in reseña_menor20:
      print('El id: ', impr[0],'tiene una reseña de: ', "{:.2f}".format(impr[2]) ) #Impresión [id,reseña media aritmética]
    
    print(' ')
    #Pregunta al usuario si desea regresar al menu principal o si quiere salir
    decision_regresarmenu=input('¿Desea regresar al menú principal? (si=1/no=cualquier tecla para salir): ')
    if decision_regresarmenu=='1': #Si la entrada fue uno solo rompre el ciclo while de la categoria reseña y vuelve al menu principal
      menu='romper bucle while menu 2'
    else:                          #Si elije otra cosa rompe todos los ciclo y termina el programa
      menu='romper bucle while menu 1'
      administrador='romper bucle principal para salir'
      print('Gracias por utilizar el servicio')
#--------------------------#


#--------------------------#
#EMPIEZA LA CATEGORIA INGRESOS Y VENTAS TOTALES
  while menu=='3':          #Si el usuario eligió 3 en el menú principal entonces se activa este while.
    menup3= input('Elija una opción: \n 1.-Datos anuales \n 2.-Datos por mes \n 3.-regresar \n Elige un NÚMERO: ') #Elección de un numero para entrar a alguna categoria
    print('  ')
    if menup3=='1':            #Si se elije  1 entonces activará la subcategoria datos anuales (por while menup3=2)
      print('Datos anuales')
    elif menup3=='2':          #Si se elije  2 entonces activará la subcategoria datos por mes (por while menup3=2)
      print('Datos por mes')
    elif menup3=='3':          #Si se elije  3 entonces regresa al menu principal rompiendo el bucle while menu  (por while menup3=3)
      print(' ')
      administrador=='1'
      menu='romper bucle while menu 3'
    else:
      print('No se ha elejido un número correcto') #Si no asigno una opcion valida le preguntará si quiere intentarlo de nuevo
      menu=input('¿Desea reintentarlo? (si=1/no=cualquier tecla para salir):')
      print('  ')
      if menu !='1': #Si elije otra tecla distitna de 1 entonces solo basta con romper administrador para romper el bucle principal
        administrador='para romper el blucle principal'
        print('Gracias por utilizar el servicio')
    
    #SUBCATEGORIA: DATOS ANUALES
    while menup3=='1': #Si el usuario eligió 1 en menup3 entonces se activa esta subcategoria.
      ventasanuales=0 #Asignamos valores igual cero para que se vayan guardando la ventas e ingres anuales.
      ingresoanual=0
      devolucion=0   #variable para indicar cuantas devoluciones hubieron del producto.
      for ventas in lifestore_sales: #Bucle para recorrer cada variable dentro de las ventas
        ventasanuales+=1 #cada iteración será una venta, por lo tanto agrega el valor a ventasanuales
        for precio in lifestore_products: #Ademas hacemos un ciclo for para recorrer la lista de productos y buscar el precio de ventas
          if precio[0]==ventas[1]: #si el id de la venta es igual a de la listra de producto entonces:
            if ventas[4]!=1: #Ademas si la venta no se devolvió (distinto el valor devolución a 1), entonces:
              ingresoanual+=precio[2] #Se agrega el precio al ingreso anual.
            else:
              devolucion+=1 #si el producto fue devuleto entonces agrega 1 producto a la variable devolución
      print('En 2020 se han tenido',ventasanuales, 'ventas,',devolucion,'devoluciones y se ha obtenido un ingreso neto anual de $', ingresoanual,'pesos mexicanos') #impresión de los datos anuales: [ventas anuales, devoluciones, ingreso anual]
      decisionmenu3=input('¿Desea ver la información de ventas e ingresos por mes? (si=1/no=cualquier tecla para regresar al menu principal):') #Preguntamos si desea ver la info por mes.
      if decisionmenu3=='1': #Si es así entonces le asignará a menup3=2 para activar el bucle de las info por mes
        menup3='2'
      else: #si no es así rompre el bucle de la subcategoria (menup3) y el de la categoria (menu) regresando al menu principal.
        menup3='romper bucle while menu menup1 anual'
        menu='romper bucle while menu 3'

    #SUBCATEGORIA: DATOS POR MES
    while menup3=='2': #Si el usuario eligió 2 en menup3 entonces se activa esta subcategoria.

      mesinfo=input('¿De qué mes necesita información de ventas e ingresos?: \n 1.Enero  2.Febrero\n 3.Marzo  4.Abril \n 5.Mayo  6.Junio \n 7.Julio  8.Agosto \n 9.Septiembre  10.Octubre \n 11.Noviembre  12. Diciembre\n 13. Volver al menú principal \n Elija un NÚMERO:') #Preguntamos al usuario que numero de mes desea ver

      #si desea ver algún mes entonces le asignaremos un número que coincida con la forma en que está escrita en la lista de ventas (01 para enero, 02 para febrero, etc.)
      if mesinfo=='1':
        mesinfo='01'
        titulo='enero'
      elif mesinfo=='2':
        mesinfo='02'
        titulo='febrero'
      elif mesinfo=='3':
        mesinfo='03'
        titulo='marzo'
      elif mesinfo=='4':
        mesinfo='04'
        titulo='abril'
      elif mesinfo=='5':
        mesinfo='05'
        titulo='mayo'
      elif mesinfo=='6':
        mesinfo='06'
        titulo='junio'
      elif mesinfo=='7':
        mesinfo='07'
        titulo='julio'
      elif mesinfo=='8':
        mesinfo='08'
        titulo='agosto'
      elif mesinfo=='9':
        mesinfo='09'
        titulo='septiembre'
      elif mesinfo=='10':
        mesinfo='10'
        titulo='octubre'
      elif mesinfo=='11':
        mesinfo='11'
        titulo='noviembre'
      elif mesinfo=='12':
        mesinfo='12'
        titulo='diciembre'
      elif mesinfo=='13':    #Si el usuario elije 13 entonces lo regresará al menu principal
        print('Regresando al menú principal...')
        print(' ')
        menup3='romper bucle while menu menup3 mensual' #rompe el bucle de la subcategoria menup3 ventas por mes y regresa a categoria
        menu='romper bucle while menu principal' #rompre el bucle para volver al menu principal
        continue
      else:
        print('No elejiste una opción valida, vuelve a intentarlo') #Si el usuario no elije una respuesta correcta vuelve a inicial el código
        print(' ')
        menup3=='2' #le asigna el valor 2 para que el bucle while de la subcategoria datos por mes siga funcionando.
        continue
      
      contador1=slice(3,5,1)  #Slice que va a extraer solo la linea de caracteres del mes
      ventasmensual=0 #variables para sumar las ventas e ingreso mensual
      sumaingreso=0
      for fechas in lifestore_sales: #Recorre los datos de las ventas para extraer fechas
        date=fechas[3]               #Toma como fecha el valor 3 de la lista de ventas pero sigue siendo la fecha completa [01/01/20 por ejem.]
        if date[contador1]==mesinfo: #Aplicamos el slice para extraer el mes y si (if) los meses coinciden:
          ventasmensual+=1 #agregamos la venta al contador
          for precio in lifestore_products: #abrimos el for para buscar el precio del producto.
            if precio[0]==fechas[0]: #Si el id del producto coincide con el id del producto vendido entonces:
              sumaingreso+=precio[2] #registra el precio y lo suma al mes
      #ventas mensuales

      print('En',titulo,'se vendieron ',ventasmensual,' unidades y hubo un ingreso de $',sumaingreso,'pesos mexicanos') #Impresión de las ventas [mes, ventas mensuales, ingresos mensuales]
      print(' ')
#--------------------------#


#--------------------------#
#EMPIEZA LA BÚSQUEDA DE ID
  while menu=='4':          #Si el usuario eligió 4 en el menú principal entonces se activa este while.
    idd=input('¿Cuál es el id que desea consultar?:') #Pregunta el número del id que desea consultar
    encuentra=0 #le damos un valor a encuentra de cero por si no se pone un id correcto
    for datos in lifestore_products:  #abrimos el for para recorrer la entrada en la lista de datos.
      if idd == str(datos[0]): #si la entrada coincide con algún id de la lista producto entonces:
        encuentra=1 #le cambia el valor a encuentra
        print('Descripción del producto:',datos[1], '\n Precio:',datos[2],'\n Categoria:',datos[3],'\n Stock:',datos[4]) #imprime la info del ide [id, precio, categoria, stock]
    if encuentra!=1: #Si no le cambio el valor a encuentra entonces se quedaría con el valor cero y por lo tanto cumple con este if:
      print('No se ha encontrado el id del producto') #Como no cumple imprime un aviso
    idrepetir=input('¿Desea buscar un nuevo id? (Sí=1/Regresar al menú de inicio=cualquier tecla): ') #independiente que encuentre o no el id le pregunta si quiere buscar uno nuevo o si quiere regresar al menu principal
    if idrepetir=='1':  #si decide que si entonces:
      menu=='4' #La da a menu==4 volviendo a activar el ciclo while de la categoria busqueda de ID
    else: #si no rompe el ciclo de la categoria y entra al while del menu principal.
      break

#FIN DEL CÓDIGO :) WUJUU  SALU2.
#EIRM