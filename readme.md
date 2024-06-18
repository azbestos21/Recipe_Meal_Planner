This is a Recipe Meal Planner done for the Fullstack Project

python -m venv venv
venv\Scripts\activate
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
