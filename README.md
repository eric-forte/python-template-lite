# python-template-lite
Lightweight Python (3.7+) Template 

## Purpose
Minimal python structure for containerized deployment with celery tasks

## Usage
This project user celery workers for data processing. The `app` is to read, process, and save data. The `io` module is a placeholder for custom data input/output needs, with initial generic implementation for `json`. 

* Replace existing tasks in `tasks.py` with desired tasks, add custom i/o operations to `io.py`, and add/replace dataclasses in `classes.py` 

* Use Makefile to deploy worker and/or run tests as desired
    * To deploy locally run `make deploy`
    * To test/submit jobs locally, run `python test.py` (after running `make deploy` and after the broker and results backend are running, e.g. rabbitmq)

* Rabbitmq is REQUIRED for this to function. One can run rabitmq in a docker container locally and use current settings via `docker run -d -p 5672:5672 rabbitmq`

* NOTE if using docker deployment for app one MUST change the ipaddress of the rabbitmq broker and results backend

## Installation (local)
1. Create a python virtual environment as desired and install the dependencies listed in `requirements.txt`
    * Create virtual environment: `python3 -m venv venv`
    * Activate virtual environment: `source venv/bin/activate` NOTE this command changes if you are using a different shell e.g. `fish` 
    * Install dependencies: `make setup` 

Now one can run `make deploy` to deploy the app locally
