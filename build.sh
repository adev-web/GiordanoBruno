
sh clear_cache.sh

pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

sh user.sh