from fastapi import FastAPI
from router import router


app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "App is running"}
