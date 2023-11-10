# Project drone_delivery_api
Rest API to manage delivery of medications using drones.

## Introduction
Development of a service via REST API that allows the management of medication loading using drones.


**IMPORTANT**
> La app esta desarrollada sobre python Django y Django Rest Framework, todos los modulos fueron instalados sobre un entorno vistual de python 3.8.10 en Ubuntu 20.04.

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

### ⚡ Use
```shell
curl -X 'POST' 'https://localhost:8000/solution?criterion=completed'
-H 'accept: application/json'
-H 'Content-Type: application/json'
-d '{
      "orders": [
         {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f3", "item": "New Order 1", "quantity": 2,
            "price": 2.5, "status": "completed", "created_at": "2023-10-07T19:41:12.294211"},
         {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f4", "item": "New Order 2", "quantity": 4,
            "price": 1.5, "status": "pending", "created_at": "2023-10-07T19:41:12.294211"},
         {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f5", "item": "New Order 3", "quantity": 2,
            "price": 0.5, "status": "canceled", "created_at": "2023-10-07T19:41:12.294211"},
         {"id": "091416a6-e6d9-4212-8d0f-8f45d2a6e3f6", "item": "New Order 4", "quantity": 3,
            "price": 3.5, "status": "completed", "created_at": "2023-10-07T19:41:12.294211"}
      ]
   }'
```

### ⚡ Test:
```shell
python -m unittest test/test_order.py
```

### ⚡ Create docker image:
1. ```shell
   docker build -t fastapi-test .
   ```
2. ```shell
   docker run -d -p 8000:8000 fastapi-test
   ```
