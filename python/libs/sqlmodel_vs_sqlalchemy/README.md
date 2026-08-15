# sqlmodel vs sqlalchemy

A mesma API de pets escrita duas vezes, para comparar as duas libs.

## Instalar

```bash
uv sync
```

## Rodar

Um de cada vez: os dois sobem na porta 8000 e usam o mesmo `database.db`.

```bash
# versao baseada no sqlalchemy
uv run v_sqlalchemy/main.py

# versao baseada no sqlmodel
uv run v_sqlmodel/main.py
```

Docs interativa: http://127.0.0.1:8000/docs

## Endpoints

```bash
# criar um pet
curl -X POST "http://127.0.0.1:8000/pets/" \
-H "Content-Type: application/json" \
-d '{
  "name": "Veludo",
  "type": "gato",
  "age": 3
}'

curl -X POST "http://127.0.0.1:8000/pets/" \
-H "Content-Type: application/json" \
-d '{
  "name": "Aurora",
  "type": "cachorro",
  "age": 9
}'

# listar todos
curl -X GET "http://127.0.0.1:8000/pets/"

# buscar por id
curl -X GET "http://127.0.0.1:8000/pets/1"

# atualizar por id (parcial: so os campos enviados mudam)
curl -X PUT "http://127.0.0.1:8000/pets/2" \
-H "Content-Type: application/json" \
-d '{
  "age": 10
}'

# deletar por id
curl -X DELETE "http://127.0.0.1:8000/pets/1"
```
