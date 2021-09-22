"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def addArt(catalog, artwork):

    lt.addLast(catalog['Art'], artwork)

  

def addArtist(catalog, artistname):

    lt.addLast(catalog['Artist'], artistname)

def newCatalog(estructuraDatos):
    

    catalog = {'Art': None,
               'Artist': None,}

    catalog['Art'] = lt.newList(estructuraDatos)
    catalog['Artist'] = lt.newList(estructuraDatos)
 

    return catalog

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def AddArtFecha(art, fechai, fechaf, Lista):
    if cmpArtworkByDateAcquiredSolo(art, fechai, fechaf):
            lt.addLast(Lista, art)
    return Lista
            
    
    

# Funciones de consulta

def escompra(artwork):
    if artwork['CreditLine'] == 'Purchase':
        return True

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
                    # Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork
    artwork1a = (artwork1['DateAcquired']).split('-')
    artwork2a = (artwork2['DateAcquired']).split('-')
    if float(artwork1a[0]) == float(artwork2a[0]):
        if float(artwork1a[1]) == float(artwork2a[1]):
            return (float(artwork1a[2]) < float(artwork2a[2]))
                
        else:
            return (float(artwork1a[1]) < float(artwork2a[1]))

    else:
        return (float(artwork1a[0]) < float(artwork2a[0]))

def cmpArtworkByDateAcquiredSolo(artwork, fechai, fechaf):
    artworka = (artwork['DateAcquired']).split('-')
    if artworka[0] != '':
        return (int(artworka[0]) >= int(fechai)) and (int(artworka[0]) <= int(fechaf))
    else: return False
   

# Funciones de ordenamiento

def Organizar(lista):
    return sa.sort(lista, cmpArtworkByDateAcquired)