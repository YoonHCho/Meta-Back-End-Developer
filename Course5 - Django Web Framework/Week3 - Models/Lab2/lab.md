The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

Learner will create a ModelForm called BookingForm using the Booking model.

## Objectives

- The Learner will practice creating a ModelForm using a model.

- The Learner will add form fields to the form as per the instructions.

- The Learner will populate a database table with data entered from a form on a webpage.

1. In `models.py`, create a class named `Booking` and create five attributes `first_name`, `last_name`, `guest_count`, `reservation_time`, `comments`
2. In `admin.py`, register the model and make sure models are imported.
3. Create `forms.py` and create a class `BookingForm` and pass `forms.ModelForm` as argument. Inside the BookingForm class, add another class for `Meta` and add 2 attributes to assign `Booking` and `__all__` to model and fields respectively.
4. Add `urls.py` and `views.py` and code accordingly so it works
5. Make and perform migration
6. Run server and type in the input fields and submit. Right click `db.sqlite3` -> `Open Database` and expand `SQLITE EXPLORER` and find the `myapp_booking`, right click `Show Table` and your record should show.
