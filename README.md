EL repositorio contiene los talleres realizados para el curso programacion II ingenieria de sistemas U de Manizales

## Taller 1

En la tabla propuesta, el estudiante elaborará un programa que permita la captura de datos básicos de un cliente del consultorio odontológico del doctor “XXX”. 
Los datos a leer de cada cliente son: Cédula, Nombre, Teléfono, Tipo de Cliente (Particular, EPS, Prepagada), Tipo de Atención (Limpieza, Calzas, Extracción, Diagnóstico), 
Cantidad, Prioridad de Atención (Normal, Urgente), Fecha de la Cita.

Para la elaboración de la actividad seguirá las siguientes acciones:

Calcular el valor de cada cita de acuerdo con los criterios que se observan en la tabla
Aplicar el uso de datos básicos, estructuras básicas y ordenamiento de datos en un lenguaje de programación.
Elaborar un programa que lea los datos de la cita de cada cliente y calcule el valor del servicio, teniendo en cuenta lo siguiente:
En cada cita se atiende un solo tipo de atención.
La cantidad siempre es 1 para la Limpieza y el diagnóstico y cualquier número mayor que cero para las calzas y la extracción de dientes.
El Valor a pagar por el cliente se calcula por la suma del valor de la cita más el valor de la atención por la cantidad.
Leer los datos de varios Clientes del consultorio odontológico y almacenarlos en un arreglo en memoria. Con los datos almacenados calcular:
Total, Clientes
Ingresos totales recibidos
Número de clientes que van para extracción de dientes.
Es necesario ordenar los clientes del consultorio odontológico en una lista ordenada por el valor de la atención de mayor a menor; posteriormente buscar en la lista ordenada un cliente con una cedula específica.

## Taller 2

El estudiante elegirá o emulará un consultorio odontológico; sobre este, adelantará un plan de contingencia para los clientes que tienen citas pendientes de extracción de piezas dentales y que además tienen carácter urgente. Por lo anterior es necesario diseñar un programa que genere una Pila de clientes para atender directamente en la clínica y los cuales van a ser llamados de acuerdo con los siguientes criterios:

Solo serán llamados los clientes que vengan para extracciones dentales.
Solo se atenderán además aquellos que tengan una prioridad de “Urgente”
La pila quedará en orden de fecha de la más cercana a la más lejana.
Generar un informe de la Pila para que en la clínica puedan llamar a los clientes y atenderlos prioritariamente.
El consultorio odontológico atenderá diariamente los clientes que llegan, los cuales serán gestionados en el estricto orden que define la agenda. Generar la agenda e ir atendiendo los clientes a través de la implementación de una Cola de atención.
