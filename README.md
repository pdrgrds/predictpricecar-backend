poetry run django-admin startproject config src/

poetry run python src/manage.py startapp api
mv api src
poetry run python src/manage.py startapp accounts
mv accounts src/

poetry run python src/manage.py makemigrations accounts
poetry run python src/manage.py migrate

poetry run python src/manage.py createsuperuser\n
poetry run python src/manage.py runserver\n

# Run docker

docker build -t predictcar .
docker run -d -p 8000:8000 predictcar