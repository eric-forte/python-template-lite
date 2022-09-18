## To check syntax use `cat -e -t -v Makefile`

test:
	python test.py

deploy:
	celery -A project worker -l INFO

setup:
	pip install -r requirements.txt

clean:
	rm -rf project/__pycache__