from mongoengine import Document,StringField,EmailField




class User(Document):
    firstName = StringField(min_length=3, max_length=50)
    lastName = StringField(min_length=3, max_length=50)
    email = EmailField(required=True, unique=True)
    phoneNumber = StringField(min_length=11, max_length=11,unique=True)
    password = StringField(min_length=6, max_length=100)
    
    
    

    

