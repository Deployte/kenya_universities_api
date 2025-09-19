from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

# --- Pretty JSON Response ---
class PrettyJSONResponse(JSONResponse):
    def render(self, content) -> bytes:
        return json.dumps(
            content,
            indent=4,
            ensure_ascii=False
        ).encode("utf-8")


# --- App Configuration ---
app = FastAPI(
    title="Kenya Universities API",
    version="1.0.0",
    description="API for accessing and filtering universities in Kenya",
    default_response_class=PrettyJSONResponse
)


# --- Load dataset once ---
DATA_FILE = os.path.join(os.path.dirname(__file__), "../../data/universities.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    UNIVERSITIES = json.load(f)


# --- Utility: normalize for case-insensitive matching ---
def normalize(s: str) -> str:
    return s.strip().lower()


# --- Root ---
@app.get("/")
async def root():
    return {
        "message": "🎓 Welcome to the Kenya Universities API!",
        "endpoints": {
            "/api/v1/universities": "Filter universities by type, category, county, or name",
            "/api/v1/universities/{id}": "Get a single university by ID",
            "/api/v1/universities/key/{key}": "Get a university by key"
        },
        "version": "1.0.0"
    }


# --- All Universities with Filters ---
# The URL now includes /v1/ for versioning
@app.get("/api/v1/universities")
async def get_universities(
    institution_type: str | None = Query(None, description="Filter by institution type (Public/Private)"),
    category: str | None = Query(None, description="Filter by category (University/University College)"),
    county: str | None = Query(None, description="Filter by location/county"),
    search: str | None = Query(None, description="Search by university name")
):
    filtered = UNIVERSITIES

    if institution_type:
        filtered = [u for u in filtered if normalize(u["institution_type"]) == normalize(institution_type)]

    if category:
        filtered = [u for u in filtered if normalize(u["category"]) == normalize(category)]

    if county:
        filtered = [u for u in filtered if county.lower() in u["location"].lower()]

    if search:
        filtered = [u for u in filtered if search.lower() in u["university"].lower()]

    if not filtered:
        return {"message": "No universities found"}
    return filtered


# --- Single University by ID ---
# The URL now includes /v1/ for versioning
@app.get("/api/v1/universities/{uni_id}")
async def get_university_by_id(uni_id: int):
    uni = next((u for u in UNIVERSITIES if u["id"] == uni_id), None)
    if not uni:
        return {"message": f"University with ID '{uni_id}' not found"}
    return uni


# --- Single University by Key ---
# The URL now includes /v1/ for versioning
@app.get("/api/v1/universities/key/{key}")
async def get_university_by_key(key: str):
    uni = next((u for u in UNIVERSITIES if normalize(u["key"]) == normalize(key)), None)
    if not uni:
        return {"message": f"University with key '{key}' not found"}
    return uni
