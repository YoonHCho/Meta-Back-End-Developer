# python manage.py shell
'''
app called myapp and in models there is a class Customer
from myapp.models import Customer

Customer.objects.get(id=4)
will get the record of an id with 4

Customer.objects.filter(reservation_day="Saturday")
will return the records with reservation_day with Saturday, filter is similar to WHERE clause in SQL

Customer.objects.filter(reservation_day="Friday") & Customer.objects.filter(seats=4)
will return records with Friday and seats are 4, & similar to AND clause in SQL
'''