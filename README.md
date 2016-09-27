
#gengue_shop


# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/local/bin/python3
or
pyvenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the git repository

```bash
git init
git remote add origin git@github.com:gengue/gengue_shop.git
```

Migrate, create a superuser, and run the server:

```bash
python gengue_shop/manage.py migrate
python gengue_shop/manage.py createsuperuser
python gengue_shop/manage.py runserver
```

Generate API docs:

```bash
npm install apidoc -g
python gengue_shop/manage.py apidoc 
```
