from app.models import User
from app import db

user1 = User(username='Billy', email='billy@gmail.com')
user1.set_password('billy')
db.session.add(user1)
db.session.commit()
print('User1 OK')

user2 = User(username='Nelly', email='nelly@gmail.com')
user2.set_password('nelly')
db.session.add(user2)
db.session.commit()
print('User2 OK')

