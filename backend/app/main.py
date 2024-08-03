from fastapi import FastAPI, Depends, Path
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.main import api_router

description = """
This is the backend API server for the Guestbook app. The Guestbook app is a simple web application that allows users to leave messages on a public guestbook.

## Guestbook

The Guestbook API allows you to perform the following operations:
- Create a new entry in the guestbook
- Read all entries in the guestbook
- Read a specific entry in the guestbook
- Update a specific entry in the guestbook
- Delete a specific entry in the guestbook
"""

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description=description,
)

# Add CORS middleware, CORS middleware is used to allow cross-origin requests
# from the frontend to the backend API server.
'''CORS stands for Cross-Origin Resource Sharing. It is a mechanism that 
allows web browsers to securely make requests to a different domain than the 
one the web page originated from.

By default, web browsers enforce a security policy called the Same-Origin 
Policy, which restricts web pages from making requests to a different domain. 
This policy is in place to prevent malicious scripts from accessing sensitive 
data or performing unauthorized actions on behalf of the user.'''

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# include routers from app/api/endpoints
app.include_router(api_router, prefix=settings.API_V1_STR)
