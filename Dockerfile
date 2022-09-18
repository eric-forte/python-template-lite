FROM --platform=linux/amd64 python:latest
RUN mkdir /app
COPY Makefile /app/Makefile
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN make setup
COPY project /app/project
COPY test.py /app/test.py 
CMD make deploy