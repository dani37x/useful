






*initialize*


```python
scheduler = APScheduler()
scheduler.init_app(app)



@scheduler.task('cron', id='get_note', second=10)
def get_notes():
    print('DZIAAAAAAAAAAAAAAAAAAAAAAALA')



scheduler.start()
```
