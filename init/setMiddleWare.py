from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware


def middelWareSetter(app,logger):
    # adding logger
    @app.middleware("http")
    async def log_exceptions(request:Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            raise e
    # adding cors
    origins = [
        "https://your-frontend-domain.com"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    