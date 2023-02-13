##? Docker Commands to run the application
run_build:
	docker build -t limebrewofficial/aot-wikis:1.0.0 .

run_api:
	docker run -it -d --name aot_wiki_api -p 8000:8000 --entrypoint  "uvicorn server:app --host '0.0.0.0' --port 8000 --reload --workers 3" limebrewofficial/aot-wikis:1.0.0  


##? Docker-Compose Commands (compose version 1)
compose_up_v1:
	docker-compose up -d --build

compose_down_v1:
	docker-compose down

compose_db_up_v1:
	docker-compose -f docker-compose.db.yml up -d --build

compose_db_down_v1:
	docker-compose -f docker-compose.db.yml down 


##? Docker Compose Commands (compose version 2)
compose_up_v2:
	docker compose up -d --build

compose_down_v2:
	docker compose down


compose_db_up_v2:
	docker compose -f docker-compose.db.yml up -d --build

compose_db_down_v2:
	docker compose -f docker-compose.db.yml down 

##? Docker Compose Command for latest version

compose_up_latest_v1:
	docker-compose -f docker-compose.test.yml up -d --build

compose_down_latest_v1:
	docker-compose -f docker-compose.test.yml down 

compose_up_latest_v2:
	docker compose -f docker-compose.test.yml up -d --build

compose_down_latest_v2:
	docker compose -f docker-compose.test.yml down 
