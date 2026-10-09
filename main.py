from fastapi import FastAPI, HTTPException
from app.router import book
from fastapi.middleware.cors import CORSMiddleware
from app.get_db import create_tables
from fastapi.responses import JSONResponse
from fastapi import Request

app=FastAPI()

create_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.exception_handler(HTTPException)
def exception_handler(request:Request,ext:HTTPException):
    return JSONResponse(status_code=ext.status_code,content={"msg":ext.detail})

app.include_router(book.router)