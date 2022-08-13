# car-info-viewer-fastapi
A little car info viewer with async database and fastapi

List of topics

* [Create a virtual environment](#section1)
    * [Minimum number of packages to install](#section1-1)
* [Create a container with postgresql](#section2)
* [General structure of this projects](#section3)
* [About configuration inside _config/_](#section4)
* [About configuration inside _connection/_](#section5)
    * [Connection configuration](#section5-1)
    * [Models configuration](#section5-2)
* [About configuration inside _schemas/_](#section6)
* [Entry point in _main.py_](#section7)
* [Alembic configuration](#section8)

<div id="section1"> </div>

# Create a virtual environment

```bash
python -m venv venv 
venv\Scripts\activate.bat
pip install -r requirements.txt
```
<div id="section1-1"> </div>

## Minimum number of packages to install

```txt
alembic
asyncpg
black
databases
email-validator
environs
fastapi
passlib[bcrypt]
psycopg2-binary
pydantic
pyjwt
pytest
requests
sqlalchemy
uvicorn
```

<div id="section2"> </div>

# Create a container with postgresql

Steps
```bash
* Download the official image
* Check the image
* Run the container with the next flags:
    * --name: container name
    * --env/-e: environment variables
    * -p: port assigment (<local>:<external>)
    * -v: where the data will be saved
    * --detach/-d: if you prefer execute it in background
* Try the connection and availability
```

Commands
```bash
docker ps
docker ps -a
docker pull postgres:latest
docker images

docker run \ 
    --name fastapi-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v C:<path>\aws-fastapi:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:latest
    
docker logs fastapi-postgres
docker exec -it fastapi-postgres bash
```

If you want to start the postgres console

```bash
docker ps
docker exec -it CONTAINER_ID bash
psql -h localhost -p 5432 -U postgres -W
\l 
CREATE DATABASE name;
\c name
\d
\dt
\q
```

<div id="section3"> </div>

# General structure of this projects

```bash
- app/
    - routers/
        - cars.py
        - products.py
    - main.py
- config/
    - .env.local
    - config.py
- databases/
    - databases.py
    - models.py
- schemas/
    - schema1.py
    - schema2.py
    ...
- static/
- templates/
- test/
    - test.py
    ...
.dockerignore
.gcloudignore
.gitignore
app.yml
Dockerfile
main.py
README.md
requirements.txt
```

<div id="section4"> </div>

# About configuration inside _config/_

```python
import os
from environs import Env

def env_reader() -> Env:
    env = Env()
    if os.path.exists("config/.env.local"):
        env.read_env("config/.env.local")
    else:
        env.read_env("config/.env.cloud")
    return env

env = env_reader()
```

<div id="section5"> </div>

# About configuration inside _connection/_

<div id="section5-1"> </div>

## Connection configuration

```python
import databases
from config.config import env

def get_database_url()->str:
    return env("DATABASE_URL")

database_url = get_database_url()
database = databases.Database(database_url)
```

<div id="section5-2"> </div>

## Models configuration

```python
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime, ForeignKey
import sqlalchemy
from connection.databases import database_url

metabase = MetaData()

Engine = Table(
    "engines",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True)
)

Maker = Table(
    "makers",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True)
)

Sold = Table(
    "solds",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True)
)

Car = Table(
    "cars",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("model", String, nullable = False),
    Column("year", Date, nullable = False),
    Column("price", Float, nullable = False),
    Column("autonomus", Float, nullable = False, server_default = False),
    Column("engine_id", ForeignKey("engines.id"), nullable = False),
    Column("maker_id", ForeignKey("makers.id"), nullable = False),
    Column("sold_id", ForeignKey("solds.id"), nullable = False)
)

engine = sqlalchemy.create_engine(database_url)
metabase.create_all(engine)
```

<div id="section6"> </div>

# About configuration inside _schemas/_

<div id="section7"> </div>

# Entry point in _main.py_

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="0.0.0.0", log_level="info", reload=True, debug=True
    )

```

And the other main file:

```python
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```

<div id="section8"> </div>

# Alembic configuration

Alembic is our migration manager

In alembic.ini 

```ini
sqlalchemy.url 
```

In migrations/env.py
```python
from connection.models import meta
target_metadata = meta
```

```bash
alembic init migrations
# Delete or change information
alembic revision --autogenerate -m "Initial"
alembic upgrade head
# Delete or change information into models file
alembic revision --autogenerate -m "Delete Test table"
alembic upgrade head
```