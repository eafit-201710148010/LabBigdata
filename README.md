# LabBigdata
en este espacio se incluye la evidencia del laboratorio de mrjob.
Se escogió el siguiente ejercicio:

2. Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción, la estructura de los datos es (archivo: dataempresas.csv):

company,price,date

exito,77.5,2015-01-01

EPM,23,2015-01-01

exito,80,2015-01-02

EPM,22,2015-01-02

…
Realizar un programa en Map/Reduce, con hadoop en Python, que permita calcular:
1.Por acción, dia-menor-valor, día-mayor-valor

2.Listado de acciones que siempre han subido o se mantienen estables.

3.DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.

la solución de los puntos se encuentra de la siguiente forma:
para el punto 1 ejecutar python mayor-menor.py companies.csv
para el punto 2 ejecutar python estables.py companies.csv
para el punto 3 ejecutar python dia-negro.py companies.csv
