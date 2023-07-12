The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

Learner will learn to use the Django admin panel.

## Objectives

- Learner will create a super user that will have administrative rights.

- Learner will create an entry for a specific user and create another new user and assign specific permissions to it using the admin panel of Django.

1. `models.py` create class `Employees` with following attributes: `first_name`, `last_name`, `role`, `shift`
2. `admin.py` register model created in step 1.
3. Open `settings.py` and make sure app config is present inside `INSTALLED_APPS` -> `myapp` or `myapp.apps.MyappConfig`
4. In the terminal, run command to make and perform migration
5. Run the command to create a super user. `python manage createsuperuser` user=admin, email=admin@littlelemon.com, password=lemonAdmin@3!
6. Run command to run server and enter login credentials just created. Go to `Employees` table under `myapp` and click `Add Employee`
7. Add following details: First name: Priya, Last name: Giti, Role: Chef, Shift: 1 and then save, notice that the `Employee object(1)` is created, but doesn't show any details - update `models.py` so that the object returns as a string. Once done, refresh to confirm it shows first name.
8. Go to `Users` in dashboard and add a new user with following: username=jason_chef, password=lemonChef@123!
9. Update permission, check mark staff status, Assign all the user permissions for `admin | log entry` to the new user. From the table `Available user permissions`, select the specific permissions by clicking on the right arrow button to move them to the `Chosen user permissions` table. then Save
