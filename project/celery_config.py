## Broker settings.
broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = ('project.tasks',)

## Using the database to store task state and results.
#result_backend = 'db+sqlite:///results.db'
result_backend = 'rpc://'
result_expires = 3600

## Hardening config
# https://progressstory.com/tech/python/production-ready-celery-configuration/
#worker_send_task_event = False
#task_ignore_result = True
# task will be killed after 60 seconds
#task_time_limit = 60  
# task will raise exception SoftTimeLimitExceeded after 50 seconds
#task_soft_time_limit = 50  
# task messages will be acknowledged after the task has been executed, not just before (the default behavior).
#task_acks_late = True 
# One worker takes 10 tasks from queue at a time and will increase the performance
#worker_prefetch_multiplier = 10  