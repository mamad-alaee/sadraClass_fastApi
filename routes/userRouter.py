from fastapi import APIRouter,Form,HTTPException,Header,Request
from validators.userValidator import UserValidator
from services.userServices import checkUserForLoginService,saveUserService,getAllUsersService,getUserByIdService,deleteUserByIdService
from init.loggerSetup import app_logger

userRouter = APIRouter()


@userRouter.get('/users')
def getALLUsers(page:int=1,limit:int=10):
    servicesResponse = getAllUsersService(page,limit)
    if servicesResponse is False:
        raise HTTPException(status_code=404, detail="No users found")
    else:
        return servicesResponse

@userRouter.get('/users/{id}')
def getUserById(id: str):
    serverResponse = getUserByIdService(id)
    if serverResponse is False:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return serverResponse

@userRouter.post('/users')
def createUser(
    firstName: str = Form(...),
    lastName: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phoneNumber: str = Form(...)
):
    try:
        userData = UserValidator(firstName=firstName, lastName=lastName, email=email, password=password, phoneNumber=phoneNumber)
        servicesResponse = saveUserService(userData.model_dump())
        if servicesResponse:
            return {"message": "User created successfully"}
        else:
            raise HTTPException(status_code=500, detail="User creation failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@userRouter.put('/users/{id}')
def updateUser(id: int):
    pass

@userRouter.delete('/users/{id}')
def deleteUser(id: str,authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        serverResponse = deleteUserByIdService(id)
        if serverResponse is False:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return {"message": "User deleted successfully"}
        


@userRouter.post('/login')
def loginUser(
        grant_type: str = Form(...),
        username: str = Form(...),
        password: str = Form(...)
):
    bodyMessage,statusCode = checkUserForLoginService(grant_type,username, password)
    raise HTTPException(status_code=statusCode, detail=bodyMessage)



@userRouter.get('/user_error')
def getUserError():
    try:
        x = 2 + 2
        raise Exception("Some error occurred")
    except Exception as e:
        error_log_data = {
            "request":str(Request),
            "error":str(e),
        }
        app_logger.error(error_log_data)