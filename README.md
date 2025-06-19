# 🧑‍💻 Flask RESTful User API

This is a simple RESTful API built with Flask, Flask-RESTful, and MongoEngine for managing user data. It supports basic CRUD operations, uses MongoDB for persistent storage, and enforces input validation.

---

## 📦 Features

- `GET /api/users` — List all users  
- `POST /api/users` — Create a new user  
- `GET /api/users/<user_id>` — Retrieve a specific user  
- `PUT /api/users/<user_id>` — Replace an existing user's data  
- `PATCH /api/users/<user_id>` — Partially update user  
- `DELETE /api/users/<user_id>` — Delete a user  
- Input validation for `email`, `age`, and `name`  
- Custom email format validator  
- Integrated with **MongoDB** using **MongoEngine (ODM)**  
- Connection configuration managed with **dotenv** (.env file)  
- Environment variables used for secure database credentials  

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- Flask
- Flask-RESTful
- MongoEngine
- python-dotenv

### Setup

1. Clone the repository.
2. Install dependencies:

   ```bash
   git clone https://github.com/Subham8989/PRODIGY_BD_02.git
   cd PRODIGY_BD_02
   pip install -r requirements.txt
