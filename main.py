from fastapi import FastAPI

app = FastAPI(
    title="Beginner FastAPI Demo",
    description="Simple FastAPI application with basic endpoints",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to my FastAPI application!"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!",
        "name": name
    }