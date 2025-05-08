from fastapi import APIRouter,Form,HTTPException
from validators.userValidator import UserValidator
from services.userServices import saveUserService,getAllUsersService,getUserByIdService,deleteUserByIdService


userRouter = APIRouter()


@userRouter.get('/users')
def getALLUsers():
    servicesResponse = getAllUsersService()
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
def deleteUser(id: str):
    serverResponse = deleteUserByIdService(id)
    if serverResponse is False:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"message": "User deleted successfully"}
        