# Project drone_delivery_api
Rest API to manage delivery of medications using drones.

## Introduction
Development of a service via REST API that allows the management of medication loading using drones.


**IMPORTANT**
> The app is developed on Python Django and Django Rest Framework, all modules were installed on a Python 3.8.10 environment on Ubuntu 20.04.
> A scheduled task was created that runs every hour, it evaluates the status of the drone's battery and saves the values ​​in a log file (drone_api.log).
> A database-cache connection (Redis) was created that contain with data of an example drone would be saved to be inserted at the beginning of the API.
> A Docker-file was created for future deployment in production.
> Database for testing we use Sqlite3 and database for production Postgresql or Mysql.
> For information on the logic followed, refer to Drones.pdf.

### ⚡ Install
1. Create dir:
   ```shell
   mkdir <custom-name> && cd <custom-name>
   ```
3. Clone repository:
   ```shell
   git clone https://github.com/dlibenp/dispatch_controller.git
   ```
4. Create virtual environment:
   ```shell
   python3 -m venv venv
   ```
6. Activate virtual environment:
   ```shell
   source venv/bin/activate
   ```
8. Install requirenment:
   ```shell
   pip install -r requirements.txt
   ```
9. Create migrations:
   ```shell
   cd core  # go into app folder
   python manage.py makemigrations
   python manage.py migrate
   ```
10. Run server:
   ```shell
   python manage.py runserver
   ```

### ⚡ URL Use: Django Rest Framework uses a default swagger that you can use just by calling the basic url <localhost:8000>
```shell
    admin/
    ^api/medication/$ [name='medication-list']
    ^api/medication\.(?P<format>[a-z0-9]+)/?$ [name='medication-list']
    ^api/medication/(?P<pk>[^/.]+)/$ [name='medication-detail']
    ^api/medication/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='medication-detail']
    ^api/drone/$ [name='drone-list']
    ^api/drone\.(?P<format>[a-z0-9]+)/?$ [name='drone-list']
    ^api/drone/(?P<pk>[^/.]+)/$ [name='drone-detail']
    ^api/drone/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='drone-detail']
    ^$ [name='api-root']
    ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
    ^media/(?P<path>.*)$
```

### ⚡ Use
1. Query - Create Drone:
```shell
curl -X POST http://localhost:8000/api/drone/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json' 
    -d '{
       "serial_number": "12345",
       "model": "Lightweight",
       "weight_limit": 500,
       "battery_capacity": 100,
       "state": "IDLE"
   }'
```
1. Query - Get Drone by ID:
```shell
curl http://localhost:8000/api/drone/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```
1. Query - Get all Drones:
```shell
curl http://localhost:8000/api/drone/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```
1. Query - Update Drone by ID:
```shell
curl -X PUT http://localhost:8000/api/drone/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json' 
    -d '{
       "serial_number": "12345",
       "model": "Lightweight",
       "weight_limit": 300,
       "battery_capacity": 20,
       "state": "IDLE"
   }'
```
1. Query - Delete Drone by ID:
```shell
curl -X DELETE http://localhost:8000/api/drone/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```
1. Query - Create Medication:
```shell
curl -X POST http://localhost:8000/api/medication/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json' 
    -d '{
       "name": "abc-123_AAA",
       "weight": 200,
       "code": "ABC_0099",
       "image": <Image>,
       "drone": "<ID>"
   }'
```
1. Query - Get Medication by ID:
```shell
curl http://localhost:8000/api/medication/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```
1. Query - Get all Medications:
```shell
curl http://localhost:8000/api/medication/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```
1. Query - Update Medication by ID:
```shell
curl -X PUT http://localhost:8000/api/medication/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json' 
    -d '{
       "name": "abc-123_ZZZ",
       "weight": 200,
       "code": "ABC_8899",
       "image": <Image>,
       "drone": "<ID>"
   }'
```
1. Query - Delete Medication by ID:
```shell
curl -X DELETE http://localhost:8000/api/medication/<ID>/ 
    -H 'Accept: application/json' 
    -H 'Content-Type: application/json'
```

### ⚡ Test:
```shell
pytest
python -m unittest tests/tests.py
```

### ⚡ Create docker image:
```shell
docker build -t drone-delivery .
docker run -d -p 8000:8000 drone-delivery
```
