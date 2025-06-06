from fastapi import FastAPI
from starlette.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def homepage():
    return JSONResponse({'hello': 'world'})
