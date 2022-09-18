# Global imports
from celery import Celery
# Local imports
from project import celery_config

app = Celery(__name__)
app.config_from_object(celery_config)


if __name__ == '__main__':
    app.start()
