# Project drone_delivery_api
Rest API to manage delivery of medications using drones.

# Ejemplo de proyecto Django para guiarnos al resolver algunas cuestiones básicas

[[_TOC_]]

# Introducción
Ejemplo de proyecto Django. Contiene varios ejemplos de APPs y códigos que pueden servir de base para resolver algunas cuestiones básicas.
Por favor, lea las **CONVENCIONES** y la sección **IMPORTANTE**, como su nombre indica, es importante leerla.

**CONVENCIONES**
- En los ejemplos de comandos, toda línea que empieza con un signo `$` representa un comando ejecutado en una terminal del sistema operativo.

Si va a iniciar un nuevo proyecto, no use este como base.
-  Genere el nuevo proyecto:
```
$ django-admin startproject mi_proyecto
```

- Use las piezas (configuraciones, APPs, requirements, etcétera) de este ejemplo que se ajusten a sus necesidades adaptándolas a los casos de uso reales.

**IMPORTANTE**
> Debe tener en cuenta que el proyecto contiene pruebas para servicios que podrían no estar disponibles.
> Se han comentado las conexiones de los eventos `post_save` de los modelos a las notificaciones NATS.
> Cuando están enlazados los eventos `post_save` de los modelos a las notificaciones NATS:
> - Si el servicio NATS no está disponible, esto genera un retardo al insertar datos en la BBDD, pues los eventos de `post_save` emiten mensajes a subjects NATS, por tanto si el servidor no está disponible, el envío de mensajes será reintentado cierta cantidad de veces.
> - Si el servicio NATS no está disponible, los ejemplos de NATS no funcionarán y esto puede generar demoras en otros ejemplos que están mezclados con los de NATS.
> - Teniendo en cuenta estas cuestiones, comente la configuración `NATS_OPTIONS` por defecto en `settings.py` y descomente la que está comentada:
```
NATS_OPTIONS = {'connect_timeout': 1, 'max_reconnect_attempts': 1}
```
> Por tanto, la conexión al servidor NATS solo se intentará una vez y si en 1 segundo no responde, se desecha y no se vuelve a intentar.
> Si el servidor de NATS está disponible, estos parámetros se pueden aumnetar a los niveles aceptables, ejemplo:
```
NATS_OPTIONS = {'connect_timeout': 4, 'max_reconnect_attempts': 60}
```
> Que es la configuración activada por defecto.

# Probar el proyecto
Si desea probar el proyecto, cree un entorno virtual e instale las dependencias:
```
$ virtualenv --system-site-packages --python=python3 mi_entorno
$ source mi_entorno/bin/activate
$ cd test_project
$ python -m pip install -r requirements.txt
```

## Migraciones
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Correr el servidor de pruebas
```
$ python manage.py runserver
```

## Datos de ejemplo
Si desea usar datos de ejemplo, una vez preparado el entorno, ejecute:
```
$ python manage.py loaddata common/fixtures/initial_data.json
```
Datos provistos:
- Superusuario: admin con contraseña admin123456
- Token de autenticación para el superusuario admin. Usado en el script test_api.py en la raíz del proyecto.

## Crear datos usando la API
**Recuerde que si están enlazados los eventos de post_save de modelos de datos a las notificaciones NATS, en caso de que el servicio NATS no esté disponible, esto puede generar cierto retardo al insertar datos**

En el directorio `api_test` ejecute:
```
$ python api_test_requests.py
```

# APP de prueba
- Define modelos básicos y vistas, plantillas HTML y URLs.
- Registra sus modelos para manejarlos por la interface CRUD del sitio administrativo.

# API REST
> Todos los proyectos de ejemplo que manipulan datos, tienen ejemplos de API rest.
> Para ejemplos de documentación de API con Swagger UI y Redoc UI, puede revisar el ejemplo de `test_redis`.

En este proyecto de ejemplo la API:
- Expone algunos modelos para interactuar con la base de datos.
> - Endpoint `/api/v1/ficheros` para interactuar con el modelo de pruebas `Fichero`, que tiene un campo de tipo `FileField`.
> - Para crear un registro con un fichero usando `curl`:
```
curl --location --request POST 'http://localhost:8000/api/v1/ficheros/' --form title="Prueba de upload por API" --form 'the_file=@"test_file.jpg"' -H 'Authorization: token d94ce70657cf1a09fbfe3d46cd13aefd765ff06a'
```
- Endpoint para descargar ficheros que subimos al modelo de pruebas, usando stream.
- Endpoint genérico que no interactúa con la base de datos.

## Pruebas de API
En el directorio `api_test` tenemos algunos ficheros de ejemplo para consumir nuestra API.

# Graphql
Para activar graphql en nuestro proyecto, debemos seguir una serie de pasos. Puede ir comprobando cada paso en el proyecto de prueba.

1. Activar la app de Graphene en nuestro `settings.py`, en la sección de `INSTALLED_APPS`:
```
#Graphql
'graphene_django',
```

2. Definir nuestros schemas.
> Para esto, estaremos probando con dos schemas:
> Primero con uno sencillo a modo introductorio.
> Después con otro más elaborado donde usaremos Relay para hacer nuestros datos amigables con los componentes de React.

3. Registrar la(s) URL(s) para exponer nuestro(s) schema(s).
Podemos registrar nuestras ULRs en el fichero `urls.py` general de nuestro proyecto.

Para simplificar, solo mostramos las partes de interés:
```
from graphene_django.views import GraphQLView

from prueba.schema import schema as schema_simple
from test_project.schema import schema as schema_complex

urlpatterns = [
    ....
    #Graphql
    path("graphql/v1/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_simple))),
    path("graphql/v2/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_complex))),
    ....
]
```