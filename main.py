from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import List, Dict

app = FastAPI(title="Rachel Phin's Personal Website")

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Personal information
PERSONAL_INFO = {
    "name": "Rachel Phin",
    "linkedin_url": "https://linkedin.com/in/rachelphin",  # Update with your LinkedIn URL
    "email": "rachel@rachelphin.com",  # Update with your email
    "github_url": "https://github.com/vishnya",
    "domain": "rachelphin.com"
}

# Sample projects data - replace with your actual projects
PROJECTS = [
    {
        "title": "Personal Website",
        "description": "A modern personal website built with FastAPI and Tailwind CSS",
        "technologies": ["Python", "FastAPI", "Tailwind CSS"],
        "link": "https://github.com/vishnya/personal_page"
    }
    # Add more projects here
]

# Sample blog posts - replace with your actual blog posts
BLOG_POSTS = [
    {
        "title": "Welcome to My Blog",
        "date": "2024-02-20",
        "preview": "Welcome to my blog where I share my thoughts and experiences...",
        "slug": "welcome-to-my-blog"
    }
    # Add more blog posts here
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "personal_info": PERSONAL_INFO
        }
    )

@app.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse(
        "projects.html",
        {
            "request": request,
            "personal_info": PERSONAL_INFO,
            "projects": PROJECTS
        }
    )

@app.get("/blog")
async def blog(request: Request):
    return templates.TemplateResponse(
        "blog.html",
        {
            "request": request,
            "personal_info": PERSONAL_INFO,
            "posts": BLOG_POSTS
        }
    )

@app.get("/blog/{slug}")
async def blog_post(request: Request, slug: str):
    # In a real application, you'd fetch the blog post from a database
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if not post:
        return templates.TemplateResponse(
            "404.html",
            {
                "request": request,
                "personal_info": PERSONAL_INFO
            }
        )
    return templates.TemplateResponse(
        "blog_post.html",
        {
            "request": request,
            "personal_info": PERSONAL_INFO,
            "post": post
        }
    ) 