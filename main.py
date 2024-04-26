import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from shared.services import MessageService
from shared.repositories import ScyllaMessageRepository
from shared.models import Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize the repository and service
# Removed due to connection issues with Cassandra/ScyllaDB in the current setup
# TODO: Implement an alternative storage solution or mock for demonstration purposes
message_service = MessageService(ScyllaMessageRepository(cluster_ips=[]))

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/list")
def list_entrypoint(page: int = 1, limit: int = 10, last_id: int = 0):
    # Example data, replace with actual data retrieval, pagination, and idempotent logic
    some_list = [{"id": 1, "data": "data1"}, {"id": 2, "data": "data2"}, {"id": 3, "data": "data3"}, {"id": 4, "data": "data4"}, {"id": 5, "data": "data5"}, {"id": 6, "data": "data6"}, {"id": 7, "data": "data7"}, {"id": 8, "data": "data8"}, {"id": 9, "data": "data9"}, {"id": 10, "data": "data10"}, {"id": 11, "data": "data11"}, {"id": 12, "data": "data12"}]
    filtered_list = [item for item in some_list if item["id"] > last_id]  # Ensure 'last_id' is already an int
    page_start = (page - 1) * limit  # Calculate the starting index of items for the current page
    page_end = page_start + limit  # Calculate the ending index of items for the current page
    return filtered_list[page_start:page_end]

# Do not remove the main function while updating the app.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")