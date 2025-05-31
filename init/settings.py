from pydantic_settings import BaseSettings




class loadSetting(BaseSettings):
    databaseName : str
    SECRECT_KEY : str
    ALGORITHM : str
    
    class Config:
        env_file = ".env"
        
        
        
settings = loadSetting()




