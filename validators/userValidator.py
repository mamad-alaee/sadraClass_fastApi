from pydantic import BaseModel,constr,EmailStr





class UserValidator(BaseModel):
    firstName : constr(min_length=3, max_length=50) # type: ignore
    lastName : constr(min_length=3, max_length=50) # type: ignore
    email : EmailStr() # type: ignore
    phoneNumber : constr(min_length=11, max_length=11) # type: ignore
    password : constr(min_length=6, max_length=100) # type: ignore