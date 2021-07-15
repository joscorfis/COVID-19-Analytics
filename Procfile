release: python ./manage.py makemigrations && python manage.py migrate && python manage.py flush --noinput
web: gunicorn covid19analyzer.wsgi --log-file -
