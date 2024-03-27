from fastapi import FastAPI
#from db.database import engine
#from db import models
#from router import user_router
#from auth import authentication

app = FastAPI()
#app.include_router(user_router.router)
#app.include_router(authentication.router)

@app.get('/testserver')
def index():
    return {
        'message': 'server is working'
    }

#models.Base.metadata.create_all(engine)