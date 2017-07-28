Читать:
- https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/с

Смотреть: 
- https://www.youtube.com/watch?v=9EftQMnuhvU&t=5s
- https://www.youtube.com/watch?v=ctLi6_mrPLc&t=882s
- https://www.youtube.com/watch?v=bC6djm33630

```
wrk -t12 -c40 -d30s http://127.0.0.1:8080/my_name
```

```
gunicorn server_aiohttp:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker --workers=4
```

```
DJANGO_SETTINGS_MODULE=project.settings_dev_pg python manage.py migrate
```


```
wrk -t12 -c40 -d30s http://127.0.0.1:8080/api/mark/
```