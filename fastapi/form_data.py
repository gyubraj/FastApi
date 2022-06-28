
# Install python-multipart
# pip install python-multipart

from fastapi import Body, FastAPI, Form

app = FastAPI()

# Form(regex='A[A-Za-z0-9@#$%^&+=]{8,}')

@app.post('/login/')
async def login(username: str = Form(), password: str = Form()):
    return {
        'username': username
    }