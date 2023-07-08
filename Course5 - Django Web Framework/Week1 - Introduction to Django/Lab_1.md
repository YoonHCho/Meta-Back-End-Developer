## Check current working directory

```
pwd
```

## Install Virtual Environment

```
pip3 install virtualenv
```

## Create a new VE named "django-venv"

```
python -m venv django-venv
OR
~/.local/bin/virtualenv django-venv
```

## Activate the VE

```
django-venv\Scripts\activate
OR
source django-venv/bin/activate
```

- You can tell that the virtual environment is activated if you see the suffix inside round brackets (django-venv) on the command prompt.

## Check if Django is installed and Create Django Project (make sure Django is installed)

To check

```
python3 -m django --version
```

If Django is not installed

**Note:** Remember to install Django while you are in the virtual environment!

```
pip3 install django
```

Once Django is installed, create projectm named `myproject`

```
django-admin startproject myproject
```

Above command will create `myproject` directory and within the directory there will be another directory called `myproject`. Or can create the project in current directory by using `.` at the end and this will not create another directory.

`cd` into `myproject` directory

```
cd myproject
```

- Need to be in the same directory that has the `manage.py` file

## Create Django App

Run command to create an app called `myapp`

```
python manage.py startapp myapp
```

## Run the Django server

```
python manage.py runserver
```

Once the server is running, visit `http://127.0.0.1:8000/`

## To exit out of VE

```
deactivate
```
