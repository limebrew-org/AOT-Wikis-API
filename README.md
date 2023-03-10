# AOT-Wikis-API
A FastAPI implementation of AOT Wikis of Characters to understand FastAPI concepts

## Run Server:
To start the server locally, run:

    uvicorn server:app --host "0.0.0.0" --port 8000 --reload --workers 3
## Build:
To build the API run `docker build`:

    docker build -t limebrewofficial/aot-wikis:1.0.0 .


## Build and Run:
To build and run directly, use `docker-compose`:

    docker-compose up -d --build

or with `docker compose`:

    docker compose up -d --build


to down the application:

    docker compose down


## Multi-platform Builds:
To build a multi-platform build for a image, use `docker buildx` and push it to `docker hub`

    docker buildx create --use  # One time step

    docker buildx build --push --platform linux/arm64/v8,linux/amd64 --tag limebrewofficial/aot-wikis:1.0.0 .


## Routes:

1. `/aot-wiki/all`: Get All Characters of AOT

2. `/aot-wiki?name=Mikasa`: Filter AOT Characters by Name

3. `/aot-wiki/:id`: Get a character by ID

4. `/aot-wiki?birth_place=Shinganshina`: Filter AOT Characters by Birth Place

5. `/aot-wiki?race=Eldian`: Filter AOT Characters by Race

6. `/aot-wiki/add`: Add a new character

7. `/aot-wiki/update/:id`: Update a character by ID