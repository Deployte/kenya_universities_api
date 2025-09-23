# Kenya Universities API 🎓  
Powered by [Deployte](https://deployte.com)\
\
An API for querying and filtering a dataset of universities in Kenya.  
This project is built using **FastAPI** and is deployed as a **Serverless Function** on **Render**.

---

## ✨ Features
- Filter universities by various criteria, including:
  - Institution type (Public / Private)
  - Category (University / University College)
  - County (Location)
  - University name
- Retrieve a single university’s details by:
  - **ID**
  - **Key** (short code)
- Fast and efficient data access by loading the dataset into memory at startup.
- Pretty-printed JSON responses (easy to read in browser or Postman).

---

## 🛠️ Technologies Used
- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+.
- **Python**: Core programming language.
- **Render**: Platform for instant, zero-configuration deployment of serverless functions.

---

## 🌍 API Endpoints

**Base URL:**  
https://api.depoyte.com

---

### 1. Filter Universities
**Endpoint:** `/api/v1/universities`  
**Method:** `GET`  
**Description:** Use query parameters to filter the list of universities. All parameters are optional.

| Parameter          | Example Value   | Description                                 |
|--------------------|-----------------|---------------------------------------------|
| `institution_type` | Public / Private| Filters universities by institution type.   |
| `category`         | University/University College      | Filters universities by category.           |
| `county`           | Nairobi         | Filters universities by county.             |
| `university`           | nairobi         | Case-insensitive search in university name. |
| `type` |universities| Filter all university names. |

**Example Usage:**

- API Endpoint:
GET /api/v1?location=Nairobi


- In a browser:  
[https://api.deployte.com/api/v1?location=Nairobi](https://api.deployte.com/api/v1?location=Nairobi)

---

### 2. Get all University names
**Endpoint:** `/api/v1?type=universities`  
**Method:** `GET`  
**Description:** Fetch all university names

**Example Usage:**
Can be used for areas such as dropdowns

- API Endpoint:
GET /api/v1?type=universities


- In a browser:  
[https://api.deployte.com/api/v1?type=universities](https://api.deployte.com/api/v1?type=universities)

---

### 3. Fetch all UNiversity keys
**Endpoint:** `/api/v1?type=keys`  
**Method:** `GET`  
**Description:** Fetch all universities keys.

**Example Usage:**

- API Endpoint:
GET /api/v1?type=keys


- In a browser:  
[https://api.deployte.com/api/v1?type=keys](https://api.deployte.com/api/v1?type=keys)

---

## 💻 Local Development

### Prerequisites
- Python 3.7 or higher

---

### 1. Clone the Repository
```bash
git clone https://github.com/Deployte/kenya_universities_api.git
cd kenya_universities_api
```
### 2. Install Dependencies

It is recommended to use a virtual environment.
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install the required packages
pip install -r requirements.txt
```
### 3. Run the Server

Start the local development server using uvicorn.

```bash
uvicorn api.v1.app:app --reload
```
- Your API will now be running locally at http://127.0.0.1:8000
- You can access the interactive API documentation (Swagger UI) at http://127.0.0.1:8000/docs





