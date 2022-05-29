#Variables que tienen como funcion ser un contador
votoj = 0
votom = 0
h=0
m=0

#MENU PARA LA SELECCION DE OPCIONES
while True:
    print()
    print("*********  Elecciones  *********")
    print()
    print('1- Candidatos')
    print('2- Vota Aqui')
    print('3- Cantidad de Votos Emitidos')
    print('4- Cantidad de Votos Por Genero')
    print('5- Candidato con Mayor Votacion')
    print('6- Porcentaje Obtenido por Cada Candidato')
    print('0- Salir')
#SELECCIONAR LA OPCION DESEADA Y CERRAR EL PROGRAMA SELECCIONANDO LA OPCION 0
    opcion = int(input('Seleccione la opcion deseada: '))
    if opcion == 0:
        break

#PRESENTACION DE CANDIDATOS
    if opcion == 1:
        print('Lista de Candidatos Presentes')
        print('Candidato #1 - Jose Manuel Garcia - Cargo - Presidente')
        print('Candidato #2 - Maria Cabral Frias - Cargo - Presidenta')
        opcion1 = (input('Presione cualquier tecla para salir al menu: '))

#SELECCION DE CANDIDATOS Y SELECCION DE GENERO MEDIANTE CONDICIONES ANIDADAS
    if opcion == 2:
        print('Selecciona un Candidato')
        print('Candidato #1 - Jose Manuel Garcia - Cargo - Presidente')
        print('Candidato #2 - Maria Cabral Frias - Cargo - Presidenta')
        voto = int(input('Selecciona (1) para el Primer Candidato, (2) Para el segundo candidato: '))
        if voto == 1:
           votoj = votoj+1
           print('Seleccionaste el Candidato #1 Jose Manuel Garcia')
        elif voto == 2:
            votom = votom+1
            print('Seleccionaste el Candidato #2 Maria Cabral Garcia')
        else:
            print("No seleccionaste ninguna opcion correcta")
#SELECCION DEL GENERO DEL VOTANTE, HACIENDO UN CONTADOR DE LOS MISMOS
        print('*** Indique su Genero: ***')
        genero = int(input('Seleccione la Opcion (1) Para HOMBRE, Seleccione la Opciones (2) Para MUJER: '))
        if genero == 1:
            h = h+1
            print('*** Seleccionaste Hombre ***')
        elif genero == 2:
            m = m+1
            print('** Seleccionaste Mujer ***')
        else:
            print('No seleccionaste ningun genero')

#VISTA DE LOS VOTOS INDIVIDUALES Y SUMA DE LOS MISMOS PARA LA PRESENTACION DE VOTOS TOTALES
    if opcion == 3:
        print('Numero de Votos Totales')
        print('Cantidad de Votos de Jose Manuel Garcia: ' + str(votoj))
        print('Cantidad de Votos de Maria Cabral Frias: ' + str(votom))
        print('Cantidad de Votos Totales: ' + str(votoj + votom))
        opcion3 = (input('Presione cualquier tecla para salir al menu: '))

#VISTA DE LOS GENEROS INDICADOS EN EL PRIMER MENU POR LOS VOTANTES   
    if opcion == 4:
        print('*** Votos por Genero ***')
        print('Votos Emitidos por Hombres: ' + str(h))
        print('Votos Emitidos por Mujeres: ' + str(m))
        opcion4 = (input('Presione cualquier tecla para salir al menu: '))

#VISTA DEL CANDIDATO CON MAYOR VOTOS
    if opcion == 5:
        print('*** Candidato con mayor cantidad de Votos ***')
        if votoj > votom:
            print('El candidato Jose Manuel Garcia Tiene la mayor cantidad de votos: ' + str(votoj))  
        else: print('El candidato Maria Cabral Frias Tiene la mayor cantidad de votos: ' + str(votom))
        opcion5 = (input('Presione cualquier tecla para salir al menu: '))
            
#CALCULO DEL PORCENTAJE TOTAL DE LOS CANDIDATOS
    if opcion == 6:
        print('*** Porcentaje Total de los Candidatos ***')
        #SUMA TOTAL DE LOS VOTOS DE AMBOS CANDIDATOS
        vt = votoj + votom
        #CALCULO DEL PORCENTAJE DE LOS VOTOS INDIVIDUALES DIVIDIDOS POR LOS VOTOS TOTALES MULTIPLICADOS POR 100, SACANDO ASI EL PORCENTAJE TOTAL DE CADA CANDIDATO
        porVj = (votoj / vt) * 100
        porVm = (votom / vt) * 100
        print('Porcentaje del Candidato #1: ' + str(porVj)+'%')
        print('Porcentaje del Candidato #2: ' + str(porVm)+'%')
        opcion6 = (input('Presione cualquier tecla para salir al menu: '))