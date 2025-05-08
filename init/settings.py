from pydantic_settings import BaseSettings




class loadSetting(BaseSettings):
    databaseName : str
    
    class Config:
        env_file = ".env"
        
        
        
settings = loadSetting()




