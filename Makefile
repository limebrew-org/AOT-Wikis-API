##? Docker Commands to run the application
run_build:
	docker build -t limebrewofficial/aot-wikis:1.0.0 .

run_api:
	docker run -it -d --name aot_wiki_api -p 8000:8000 --entrypoint  "uvicorn server:app --host '0.0.0.0' --port 8000 --reload --workers 3" limebrewofficial/aot-wikis:1.0.0  

##? Docker-Compose Commands 
compose_up:
	docker-compose up -d --build

compose_down:
	docker-compose down

##? Docker Compose Commands
compose_up_fix:
	docker compose up -d --build

compose_down_fix:
	docker compose down