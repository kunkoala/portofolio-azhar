
from fastapi import FastAPI, Depends, Path
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.main import api_router

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Add CORS middleware, CORS middleware is used to allow cross-origin requests
# from the frontend to the backend API server.

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''CORS stands for Cross-Origin Resource Sharing. It is a mechanism that 
allows web browsers to securely make requests to a different domain than the 
one the web page originated from.

By default, web browsers enforce a security policy called the Same-Origin 
Policy, which restricts web pages from making requests to a different domain. 
This policy is in place to prevent malicious scripts from accessing sensitive 
data or performing unauthorized actions on behalf of the user.'''


# include routers from app/api/endpoints

app.include_router(api_router, prefix=settings.API_V1_STR)








