help:
	cat Makefile
init: # init python envs
	chmod a+x ./init.sh && ./init.sh

run:
	uvicorn app.main:app

dev:
	uvicorn app.main:app --reload
