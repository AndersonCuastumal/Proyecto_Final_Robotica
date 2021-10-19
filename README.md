# Proyecto_Final_Robotica
## Planta de Empaque pasos de ejecucion.

1. Abrir la terminal y ejecutar la siguiente comando.
$ roslaunch ur5_gazebo empacar_cubos.launch

3.Esperar hasta que gazebo haya completado su inicio.

2.Abrir una nueva terminal y ejecutar la siguiente comando.
$ rosservice call gazebo/unpause_physics

3.En la misma terminal ejecutar el siguiente comando.
$ rosrun ur5_gazebo empacar.py

4. Listo

## Recomendaciones:
-Crear un "NuevoEspaciodeTrabajo" y agregar el contenido de la carpeta src de este proyecto en el nuevo "NuevoEspaciodeTrabajo" .


