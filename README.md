# Concept

## About
Adaptation of the game "concept" using Django

In this game you have to guess the secret word only with their concepts

## Running

- Clone this repository
```
git clone https://github.com/ARJOM/concept.git
```
- Create a virtual environment
```
python3 -m venv venv
```
- Start your virtual environment
```
source venv/bin/activate
```
- Upgrade pip
```
python -m pip install --upgrade pip
```
- Install Django
```
pip install -r requirements.txt
```
- Create a Super User
```
python manage.py createsuperuser
```
- Perform the migrations
```
python manage.py makemigrations core
python manage.py makemigrations game
python manage.py migrate
```
- Run the project
```
python manage.py runserver
```
