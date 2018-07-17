from app.models import User, Post
from app import db

billy_id = User.query.filter_by(username='billy')
id = None
for x in billy_id:
	id = x.id
post_billy = Post(body='My first post. Im Billy.', user_id=id)
db.session.add(post_billy)
db.session.commit()
print('Post_Billy OK')

nelly_id = User.query.filter_by(username='nelly')
id = None
for x in nelly_id:
	id = x.id
post_billy = Post(body='My first post. Im Nelly.', user_id=id)
db.session.add(post_billy)
db.session.commit()
print('Post_Nelly OK')


nelly_id = User.query.filter_by(username='nelly')
id = None
for x in nelly_id:
	id = x.id
post_billy = Post(body='My two post. Im Nelly.', user_id=id)
db.session.add(post_billy)
db.session.commit()
print('Post_Nelly OK')