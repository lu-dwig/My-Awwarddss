git switch master
python manage.py collectstatic
heroku config:set ALLOWED_HOSTS=dry-coast-64447.herokuapp.com
heroku config:set DEBUG=False
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set MODE=prod
heroku config:set SECRET_KEY='django-insecure-tnfjal$7+z-fn61jnc!&$)k)#j(14losqo-h6koer+@2rtim*-'

pip freeze > requirements.txt
git add .
git commit -m "heroku deployment"
git push heroku master



heroku run python manage.py makemigrations
heroku run python manage.py migrate
 
# heroku pg:push <The name of the db in the local psql> DATABASE_URL --app <heroku-app>
heroku open