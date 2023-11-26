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
5. Your blog will be seen in url

'''
http://127.0.0.1:8000/blog/<int>/
'''