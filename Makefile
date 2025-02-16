.PHONY: up down shell test lint


up:
    docker-compose up -d


down:
    docker-compose down


shell:
    docker-compose exec web bash


test:
    pytest


lint:
    ruff check .