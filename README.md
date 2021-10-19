# Proyecto_Final_Robotica
## Planta de Empaque 
### Descripción
En este proyecto se realizo una planta de empaquetado donde se hace uso del brazo robotico UR5 quien se encarga de la tarea, este toma un objeto de la banda transportadora y lo traslada a la mesa justo a la posición deseada que se le asigno.
### Limitaciones
1. Este sistema no es capaz de detectar un objeto y capturarlo.
2. La cinematica del robot esta diseñada para que el robot capture objetos inmobiles fijados en una posición especifica dada por el diseñador.
3. El UR5 adopta una postura deseada dependiendo de la posición deseada.
4. No se agrego la caja donde se ubican los cubos.
### Conclusiones
1. El area de robotica tiene un gran potencial en el area industrial como lo pudimos observar en el desarrollo de este proyecto donde un robot mediante el acople de diversas herramientas se puede optimizar su funcionamiento.
2. En la robotica es importante la precision cuando se trata de la manipulación de objetos blandos, delicados, mayor peso, etc.. Ya que un mal movimiento puede significar el daño del objeto.
3.  

### Pasos de ejecucion.
1. Abrir la terminal y ejecutar la siguiente comando.
$ roslaunch ur5_gazebo empacar_cubos.launch

2.Esperar hasta que gazebo haya completado su inicio.

3.Abrir una nueva terminal y ejecutar la siguiente comando.
$ rosservice call gazebo/unpause_physics

4.En la misma terminal ejecutar el siguiente comando.
$ rosrun ur5_gazebo empacar.py

5. Listo

### Recomendaciones:
-Crear un "NuevoEspaciodeTrabajo" y agregar el contenido de este proyecto en el nuevo "NuevoEspaciodeTrabajo" .




