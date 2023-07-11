# Neximo Test con DJANGO

### Este readme contiene las instrucciones para ejecutar el codigo del repositorio

## Requisitos previos
    - Docker, asegurate de tener docker instalado en tu sistema, puedes descargar el ejecutable de la pagina principal https://www.docker.com/


## Descarga y ejecucion
Sigue los pasos para descargar el repositorio y ejecutar el codigo con docker

1. Clona el repositorio en tu maquina, el link del repositorio es  : https://github.com/EedgarHM/drf_neximo_test y puedes clonarlo usando la siguiente instruccion
    - git clone https://github.com/EedgarHM/drf_neximo_test.git
    Asegurate de ejecutar el comando en la terminal cmd 
2.- Accede al directorio del proyecto en tu terminal usando el comando cd /ruta/donde/clonaste/el/repositorio

3.- Inicia el contenedor de docker usando el comando docker  run -it drf_neximo_test-app | Puede funcionar si ejecutas docker-compose up

4.- si el contenedor ejecuto correctamente ya podras acceder en el navegador a la ruta localhost:8000/api/register y  localhost:8000/api/login


## Nota importante
No se agrego funcionalidad de redireccion a la ruta localhost:8000/api/payments en el navegador, por lo que tus peticiones deberas ahcerlas con curl desde la terminals