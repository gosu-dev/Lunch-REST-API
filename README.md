To run this project use the following commands:

Using Python:
```
git clone `repository_link`

cd `path to project`

python3 -m venv venv 

pip install -r requirements.txt

```
Set up your postgres credentials in file named _'/config/settings'_

Final steps:
```
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```
Congrats, application is running. 

Using Docker:
```
docker build .

docker-compose up
```
To stop Docker container use:
```
docker-compose down
```

App can be accessed using the following address:

_127.0.0.1:8000_

