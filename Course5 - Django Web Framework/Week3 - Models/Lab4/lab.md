The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

Learner will create and connect to a MySQL database that can be used inside a Django project.

## Objectives

- Learner will create new MySQL database.

- Learner will update the project settings in Django to enable connection with MySQL.

1. Run the command that will enable access to MySQL `mysql -u root -p` **Note**: The default password set for mysql here will be blank. What it means is, when you receive a prompt for entering password, you will simply press the Enter key on your keyboard.
2. Run command to show the databases present already `show databases;`. Then create a new database `feedback` -> `CREATE DATABASE feedback`. Check if the newly created database is present. If not already installed, install `mysqlclient`. Run command to exit the MySQL shell `exit`
3. Project level `settings.py` go to `DATABASES` option and replace it with following code:

   ```
   'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'feedback',
     'HOST': '127.0.0.1',
     'PORT': '3306',
     'USER': 'root',
     'PASSWORD': '',
   }
   ```

4. In terminal, run command to make and perform migration.
