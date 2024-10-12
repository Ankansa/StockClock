from fastapi import FastAPI
from app.routes.item_routes import router as item_router
from app.routes.clock_in_routes import router as clock_in_router

app = FastAPI()

# Registering the routes
app.include_router(item_router, prefix="/items", tags=["Items"])
app.include_router(clock_in_router, prefix="/clock-in", tags=["Clock-In Records"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD App!"}
