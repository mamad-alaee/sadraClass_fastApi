from models.userModel import User
from bson.objectid import ObjectId




def saveUserService(userData):
    try:
        user = User(**userData)
        user.save()
        return True
    except Exception as e:
        return False
    
    
def getAllUsersService():
    try:
        usersList = list(User.objects().as_pymongo())
        if len(usersList) == 0:
            return False
        else:
            for user in usersList:
                user["_id"] = str(user["_id"])
            return usersList
    except Exception as e:
        return False
    
def getUserByIdService(userId):
    try:
        user = User.objects(id=ObjectId(userId)).as_pymongo()[0]
        if user:
            user["_id"] = str(user["_id"])
            return user
        else:
            return False
    except Exception as e:
        return False
    
def deleteUserByIdService(userId):
    try:
        user = User.objects(id=ObjectId(userId))
        if user :
            user.delete()
            return True
        else:
            return False
    except Exception as e:
        return False
            