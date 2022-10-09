A Basic To-Do Web Application built-on Django Framework. Here the user can create, update and delete the task which is existing. Using sqlite3 the data has been stored in the Application.

Features:
    • Add Task
    • Delete Task
    • Mark as Completed
    • List of Tasks
    • List of Completed Tasks
    • List of Pending Tasks


Steps to be followed for first time use
Run these commands - This will create your Tables (by the Model definition) in the Database

python manage.py makemigrations

python manage.py migrate



Create an admin user by running these following commands
$ python manage.py createsuperuser

admin url can be acessed by http://127.0.0.1:8000/admin/

