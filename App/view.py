﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportarcobras de un departamento ")
    print("7- Proponer una nueva exposición en el museo")
    

catalog = None


def initCatalog():
    """
    Inicializa el catalogo o
    """
    return controller.initCatalog(TipoEstructura)


def loadData(catalog):

    controller.loadData(catalog)
"""
Menu principal
"""
TipoEstructura = 'SINGLE_LINKED'
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        input1 = input('Seleccione una opción para continuar\n'+
                        'Presione 1 para cargar la lista como un Array List\n' +
                         'Presione 2 para cargar la lista como un Linked List\n')
        if int(input1) == 1:
            #Cargar como Array List
            TipoEstructura = 'ARRAY_LIST'
            print("Se ha configurado como Array List")
            
        elif int(input1) == 2:
            #Cargar como Linked List
            TipoEstructura = 'SINGLE_LINKED'
            print("Se ha configurado como Linked List")
            
            
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))
        print('Obras cargados: ' + str(lt.size(catalog['Art'])))
        print('Ultimos 3 artistas: ') #+ str(lt.size(catalog[''])))
        print('Ultimas 3 obras ' ) #str(lt.size(catalog[''])))
    elif int(inputs[0]) == 3:
        input1 = int(input('Ingrese la fecha inicial '))
        input2 = int(input('Ingrese la fecha final '))
        Resultado = (controller.Req2(catalog, input1, input2))
        print('La lista organizada es: ')
        print(Resultado[0])
        print('El numero total de obras en el rango es: ')
        print(Resultado[1])
        print('El total de obras en el rango adquiridas por compra es: ')
        print(Resultado[2])
    else:
        sys.exit(0)
sys.exit(0)
