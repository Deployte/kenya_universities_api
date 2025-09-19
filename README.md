# Kenya Universities API 🎓

An API for querying and filtering a dataset of universities in Kenya.  
This project is built using **FastAPI** and is deployed as a **Serverless Function** on **Vercel**.

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
- **Vercel**: Platform for instant, zero-configuration deployment of serverless functions.

---

## 🌍 API Endpoints

**Base URL:**  
https://kenya-universities-kh4vb7mmn-deployte.vercel.app?_vercel_share=F5stIxxnG4xWAejsUwpPTBinvI7JZLNH

---

### 1. Filter Universities
**Endpoint:** `/api/universities`  
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
GET /api/universities?institution_type=Public&county=Nairobi


- In a browser:  
[https://https://kenya-universities-kh4vb7mmn-deployte.vercel.app?_vercel_share=F5stIxxnG4xWAejsUwpPTBinvI7JZLNH/api/universities?institution_type=Public&county=Nairobi](https://kenya-universities-kh4vb7mmn-deployte.vercel.app?_vercel_share=F5stIxxnG4xWAejsUwpPTBinvI7JZLNH/api/universities?institution_type=Public&county=Nairobi)

---

### 2. Get a Single University by ID
**Endpoint:** `/api/universities/{id}`  
**Method:** `GET`  
**Description:** Fetch a single university by its unique **ID**.

**Example Usage:**

- API Endpoint:
GET /api/universities/1


- In a browser:  
[https://kenya-universities-api.onrender.com/api/universities/1](https://kenya-universities-api.onrender.com/api/universities/1)

---

### 3. Get a University by Key
**Endpoint:** `/api/universities/key/{key}`  
**Method:** `GET`  
**Description:** Fetch a single university by its unique **Key**.

**Example Usage:**

- API Endpoint:
GET /api/universities/key/UON


- In a browser:  
[https://kenya-universities-api.onrender.com/api/universities/key/UON](https://kenya-universities-api.onrender.com/api/universities/key/UON)

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
uvicorn api.app:app --reload
```
- Your API will now be running locally at http://127.0.0.1:8000
- You can access the interactive API documentation (Swagger UI) at http://127.0.0.1:8000/docs

