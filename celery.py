from celery import Celery


app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

#creates a Celery object
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


from project_files import celery


import time

@celery.task
def async_function(arg1, arg2):
    result = arg1 + arg2
    while True:
        time.sleep(5)
        print(result)
        
async_function()
