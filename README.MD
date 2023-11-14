1. Install dependencies:

'''
pip install -r requirements.txt
'''

2. Run docker process:

'''docker run -p 6379:6379 redis'''

3. Create 'int' number blogs

'''
python manage.py create_blogs 'int'
'''

4. Run Django webserver 

'''
python manage.py runserver
'''
