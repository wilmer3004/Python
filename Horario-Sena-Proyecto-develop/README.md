# Horario-Sena-Proyecto
El repositorio cuenta con un proyecto para la gestión de horarios en el cual se cargaran de acuerdo a la rama avances del proyecto este repositorio solo contara con el back-end del proyecto


Prerequisitos :
-Se debe de tener instalada una version de python superior o igual a la version 3.10.11
-Se debe de tener un editor de código de preferencia, recomendación (Visual Studio Code)

Pasos para que el proyecto pueda funcionar:
- Se verifica que en la terminal estemos dentro del proyecto al estar en la carpeta Horario-Sena-Proyecto dentro de la terminal

-Se debe de crear un entorno virtual con los siguientes pasos:
    -Se ingresa a la terminal y se instala la dependencia de virtualenv con el siguiente código:
        pip install virtualenv

    -Se Procede a crear el entorno virtual con el código:
        python -m virtualenv venv

    -Em algunos casos en los sistemas operativos como windowa antes de activar el entorno virtual es necesario utilizar el siguiente codigo para configurar las politicas:
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    -Para activar el entorno virtual utilizamos el siguiente código:
        En Windows, ejecuta:
        .\venv\Scripts\activate

        En Unix o MacOS, ejecuta:
        source venv/bin/activate

-Se debe de crear un archivo que se llame ".env" dentro de la carpeta Horario-Sena-Proyecto en el cual gestionaremos las variables de entorno para la configuración del proyecto y asi mismo la conexión a la base de datos, dentro de este mismo ira la siguiente información:

    estos datos si son fijos en el archivo .env
    SECRET_KEY=192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf
    JWT_KEY=D5*F?_1?-d$f*1

    Estos datos varia de acuerdo a lo que se obtenga de la base de datos virtual temporal a la cual se accede con las siguientes credenciales en clever cloud (https://console.clever-cloud.com/), correo "horariossena92@gmail.com" contraseña "hsena123*" es necesario acceder a Me personal space, luego database y en admin estaran los datos para la respectiva coneccion:
    
    El siguiente codigo es un ejemplo de como debe ir en el archivo .env 
    
        MYSQL_HOST= bik2mxrnxuyab2ivw78t-mysql.services.clever-cloud.com
        MYSQL_USER= ujt0etbl1d1srcca
        MYSQL_PASSWORD= pjc5uRNxFLQaRVagW8Wy
        MYSQL_DB= pjc5uRNxFLQaRVagW8Wy

    En caso de que la base de datos sea local se debe de crear la base de datos en workbench con el codigo que se encuentra en database.txt y la coneccion seria de la siguiente manera
        MYSQL_HOST= localhost
        MYSQL_USER= root
        MYSQL_PASSWORD=
        MYSQL_DB= dbhorariosena

-El archivo .env al finalizar debe tener los siguientes datos de acuerdo a las anteriores especificaciones.
    SECRET_KEY=192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf
    JWT_KEY=D5*F?_1?-d$f*1
    MYSQL_HOST= bik2mxrnxuyab2ivw78t-mysql.services.clever-cloud.com
    MYSQL_USER= ujt0etbl1d1srcca
    MYSQL_PASSWORD= pjc5uRNxFLQaRVagW8Wy
    MYSQL_DB= pjc5uRNxFLQaRVagW8Wy



-Se deben de instalar todas las dependencias ya sea una por una o mediante el archivo requirements.txt

-Es necesario tener la base de datos creada esta misma esta para poderce ejecutar en workbeanch en el script que hay en database.txt

-Para poder recorrer el proyecto se necesita de correr o debuguear el archivo index.py

-En caso de que se ingresen nuevas dependencias se elimina el archivo requirements.txt y se ejecuta el siguiente codigo para almacenarlas
    pip freeze > requiremets.txt


