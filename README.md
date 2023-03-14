# Cards API em Django Rest Framework

## Stacks usacdas:
- Django Rest Framework (API)
- Docker (Containering the app and all the services and db) 
- Postgres (store data into database)
- Swagger (Documentação)
- Redocs (Documentação)


## Passos
- Apenas rodar o comando a primeira vez: ```docker-compose up --build```,
depois rodar: ```docker-compose up```,
Uma vez que o docker está rodando você poderá realizar os tests da API


### Eu estou enviando um export das requisições do postman, Arquivo:
```Globo.postman_collection.json```,
Basta importar no postman e testar a API

### Username padrão para o django admin
``
username = admin,
password = mystrongpassword
``

Sinta se a vontade para criar outro super usuário usando o comando: ```python manage.py createsuperuser``` dentro do docker


## Adicionado casos de testes usando APITestCase
Basta rodar dentro do dockar:
```docker-compose run api bash```
então:
```python manage.py test```

## Rodando o comando de importar cards via CSV
basta rodar dentro do dockar:
```docker-compose run api bash```
então:
```python manage.py  import_csv --csv_file=caminho_do_arquivo+.csv```

## Swagger
basta subir o docker:
```docker-compose up```
então no seu navegador navegie até:
```http://127.0.0.1:8000/```

## Documentação
basta subir o docker:
```docker-compose up```
então no seu navegador navegie até:
```http://127.0.0.1:8000/docs/```