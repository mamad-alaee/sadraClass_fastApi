from models.userModel import User
from bson.objectid import ObjectId
from jose import jwt
from init.settings import settings



def saveUserService(userData):
    try:
        user = User(**userData)
        user.save()
        return True
    except Exception as e:
        return False
    
    
def getAllUsersService(page,limit):
    try:
        skip = (page-1)*limit
        usersList = list(User.objects().skip(skip).limit(limit).as_pymongo())
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
            
            
def checkUserForLoginService(grant_type,username, password):
    try:
        if grant_type == "email":
            user = User.objects(email = username).as_pymongo()[0]
            if user is None:
                return {"message": "User not found"},404
            else:
                if user["password"] == password:
                    return create_access_token({"user_id":str(user["_id"])})
                else:
                    return {"message": "Invalid password"},401
        elif grant_type == "phone":
            pass
        else:
            return {"message":"Invalid grant_type"},400
    except Exception as e:
        print(e)
        return {"message": "Something went wrong","error":e},500
    
    
def create_access_token(userData):
    jwt_token = jwt.encode(userData,key=settings.SECRECT_KEY, algorithm=settings.ALGORITHM)
    return {"access_token":jwt_token},200
    