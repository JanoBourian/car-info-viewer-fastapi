# car-info-viewer-fastapi
A little car info viewer with async database and fastapi

List of topics

* [Create a virtual environment](#section1)
    * [Minimum number of packages to install](#section1-1)
* [Create a container with postgresql](#section2)
* [General structure of this projects](#section3)
* [About configuration inside _config/_](#section4)
* [About configuration inside _databases/_](#section5)
* [About configuration inside _schemas/_](#section6)

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
    - routers
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

<div id="section5"> </div>

# About configuration inside _databases/_


<div id="section6"> </div>

# About configuration inside _schemas/_