from routes.userRouter import userRouter




def setRoutes(app):
    app.include_router(userRouter)