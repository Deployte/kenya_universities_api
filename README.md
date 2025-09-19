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
https://kenya-universities-api.onrender.com

---

### 1. Filter Universities
**Endpoint:** `/api/v1/universities`  
**Method:** `GET`  
**Description:** Use query parameters to filter the list of universities. All parameters are optional.

| Parameter          | Example Value   | Description                                 |
|--------------------|-----------------|---------------------------------------------|
| `institution_type` | Public / Private| Filters universities by institution type.   |
| `category`         | University      | Filters universities by category.           |
| `county`           | Nairobi         | Filters universities by county.             |
| `search`           | nairobi         | Case-insensitive search in university name. |

**Example Usage:**

- API Endpoint:
GET /api/v1/universities?institution_type=Public&county=Nairobi


- In a browser:  
[https://kenya-universities-api.onrender.com/api/v1/universities?institution_type=Public&county=Nairobi](https://kenya-universities-api.onrender.com/api/v1/universities?institution_type=Public&county=Nairobi)

---

### 2. Get a Single University by ID
**Endpoint:** `/api/v1/universities/{id}`  
**Method:** `GET`  
**Description:** Fetch a single university by its unique **ID**.

**Example Usage:**

- API Endpoint:
GET /api/v1/universities/1


- In a browser:  
[https://kenya-universities-api.onrender.com/api/v1/universities/1](https://kenya-universities-api.onrender.com/api/v1/universities/1)

---

### 3. Get a University by Key
**Endpoint:** `/api/v1/universities/key/{key}`  
**Method:** `GET`  
**Description:** Fetch a single university by its unique **Key**.

**Example Usage:**

- API Endpoint:
GET /api/v1/universities/key/UON


- In a browser:  
[https://kenya-universities-api.onrender.com/api/v1/universities/key/UON](https://kenya-universities-api.onrender.com/api/v1/universities/key/UON)

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




