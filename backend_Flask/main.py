from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
) 

users=["alla ismail"]

@app.get("/users")
async def get_users():
    return users

@app.post("/users")
async def create_user(user):
    users.append(user)
    return "succes posted"
