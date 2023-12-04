# Pasos para ejecutar el proyecto

Primero hay que cambiar los valores que se encuentran en los comentarios TODO: luego hay que correr el archivo

***process_get_values.py***

Este archivo lo que hará es obtener las garantías que se enviarán con valor 0 al FGA ya que calcula el valor que
hace falta y lo llena con los valores de las garantías vigentes.

Una vez hecho el punto anterior procedemos a añadir el encabezado ***pagare,fecha_corte,valor_comision_reportado***
en el archivo de success_lineru_list.csv y posteriormente ejecutamos el archivo de python:

***filtering_files_csv.py***

Para obtener el archivo data_review.csv que nos da el valor de las garantías que se procesarán posteriormente.
Ahora corremos el programa:

***filtering_files_csv_inverted.py***

Para obtener ***data_review_2.csv*** que es el que se pondrá en el proyecto principal del FGA, este archivo reemplazará a ***new_apps.csv***

***data_review_2.csv*** ==> ***new_apps.csv***

Finalmente corremos el programa

***update_with_value.py***

Y esperamos a que se actualicen los valores.