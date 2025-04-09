# Import APIRouter to organize routes
from fastapi import APIRouter

# Create a router instance to define routes under this file
router = APIRouter()

# Define a GET route to handle '/workloads' requests
@router.get("/workloads")
def get_workloads():
    # Return a basic JSON response
    return {"message": "List of AI workloads"}
