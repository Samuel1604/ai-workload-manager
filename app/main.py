# Import FastAPI to create the main app
from fastapi import FastAPI

# Import the workload route module from app.routes
from app.routes import workload

# Create an instance of FastAPI with a custom title
app = FastAPI(title="AI Workload Management API")

# Include the router we defined in workload.py so that
# its routes become part of the app
app.include_router(workload.router)
