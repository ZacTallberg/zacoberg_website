web: gunicorn griffin_app.wsgi --workers=4 --bind 0.0.0.0:$PORT --log-file=-
worker: python manage.py process_tasks
