import os, json
from fastapi import FastAPI, Query

DATA_FILE = os.path.join(os.path.dirname(__file__), "../universities.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    universities = json.load(f)

app = FastAPI(
    title="Kenya Universities API",
    description="API for accessing universities in Kenya",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "🎓 Welcome to the Kenya Universities API!"}



@app.get("/universities", response_model=List[dict])
def get_universities(
    institution_type: Optional[str] = Query(None, description="Filter by institution type (e.g. Public, Private)"),
    category: Optional[str] = Query(None, description="Filter by category (e.g. University, University College)"),
    county: Optional[str] = Query(None, description="Filter by location/county"),
    search: Optional[str] = Query(None, description="Search by university name")
):
    results = universities

    if institution_type:
        results = [u for u in results if normalize(u["institution_type"]) == normalize(institution_type)]

    if category:
        results = [u for u in results if normalize(u["category"]) == normalize(category)]

    if county:
        results = [u for u in results if county.lower() in u["location"].lower()]

    if search:
        results = [u for u in results if search.lower() in u["university"].lower()]

    return results


@app.get("/universities/{uni_id}", response_model=dict)
def get_university_by_id(uni_id: int):
    uni = next((u for u in universities if u["id"] == uni_id), None)
    if not uni:
        raise HTTPException(status_code=404, detail="University not found")
    return uni


@app.get("/universities/key/{key}", response_model=dict)
def get_university_by_key(key: str):
    uni = next((u for u in universities if normalize(u["key"]) == normalize(key)), None)
    if not uni:
        raise HTTPException(status_code=404, detail="University not found")
    return uni
