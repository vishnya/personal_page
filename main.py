from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "name": "Your Name",  # Replace with your name
            "linkedin_url": "https://linkedin.com/in/your-profile",  # Replace with your LinkedIn
            "email": "your.email@example.com"  # Replace with your email
        }
    )

@app.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse(
        "projects.html",
        {
            "request": request,
            "projects": [
                {
                    "title": "Project 1",
                    "description": "Description of project 1",
                    "link": "#"
                }
                # Add more projects here
            ]
        }
    )

@app.get("/blog")
async def blog(request: Request):
    return templates.TemplateResponse(
        "blog.html",
        {
            "request": request,
            "posts": [
                {
                    "title": "First Blog Post",
                    "date": "2024-02-20",
                    "preview": "Preview of the blog post..."
                }
                # Add more blog posts here
            ]
        }
    ) 