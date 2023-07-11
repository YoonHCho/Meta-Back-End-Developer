The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

To create a model, learn to perform migrations and track changes in the model. Objectives

- The learner will create a model called Drinks.
- The learner will perform the steps required to apply migrations

1. Open `models.py` and create a class called `Drinks` with 2 attributes called `drink` and `price`
2. Open `admin.py` and register the Model just created
3. Cd into the project and run the dev server (Note: this will generate the `db.sqlite3` database used by default in Django)
4. Run command to make migrations and then run command to perform the migration
5. Once you are sure migrations ran successfully, modify the attribute from `drink` to `drink_name` in `models.py` and run commands (2 commands) required to perform migration.
6. Run command to show the migration changes
7. Right click `db.sqlite3` and select `Open Database`, it will have a menu for `SQLITE EXPLORER` at the bottom of the left pane. Expand the `SQLITE EXPLORER` and expand `db.sqlite3` and scroll down and check if `myapp_drinks` table is generated (No contents inside since the table is empty)
