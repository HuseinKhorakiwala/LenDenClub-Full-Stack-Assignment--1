# Secure User Profile & Access Control System

## Project Overview

This project implements **Assignment 1: Secure User Profile & Access Control System**, focused on building a secure identity management microservice with encrypted storage of sensitive user data.

The system provides:
- Secure user authentication using JWT (stateless)
- Encrypted storage of sensitive Aadhaar/ID data at rest
- Authenticated APIs to fetch and manage user profile data
- A clean React-based frontend dashboard to interact with the backend securely

The backend is built using **Django + Django REST Framework**, while the frontend is built using **React**. Special attention is given to data security, encryption, and proper separation of concerns between backend and frontend.

---

## Tech Stack

### Backend
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- Cryptography (Fernet – AES-based encryption)
- SQLite (persistent database)

### Frontend
- React (Vite)
- Axios
- Minimal custom CSS (no heavy UI libraries)


## Setup / Run Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+
- npm


### Backend Setup

```
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Create a .env file inside the backend/ directory:
``
AADHAAR_ENCRYPTION_KEY=<your-generated-fernet-key>
``

Run migrations and start the server:
```
python manage.py migrate
python manage.py runserver
```

Backend runs at:
``
http://127.0.0.1:8000
``

Frontend runs at:
``
http://localhost:5173
``
API Documentation
Authentication
Register User
POST /api/register/
``
{
  "username": "user01",
  "email": "user01@test.com",
  "password": "test1234"
}
``
Login User
POST /api/login/
``
{
  "username": "user01",
  "password": "test1234"
}
``

Response:
``
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
``
User Profile (Authenticated)

All profile APIs require:

Authorization: Bearer <access_token>

Fetch Profile
GET /api/profile/


Response:
``
{
  "username": "user01",
  "email": "user01@test.com",
  "aadhaar": "123456789012"
}
``
Update Aadhaar
POST /api/profile/
``
{
  "aadhaar": "123456789012"
}
``
Database Schema
User Model

| Field             | Type         | Description                |
| ----------------- | ------------ | -------------------------- |
| id                | BigAutoField | Primary key                |
| username          | CharField    | Unique username            |
| email             | EmailField   | User email                 |
| password          | Hashed       | Stored securely            |
| aadhaar_encrypted | TextField    | Encrypted Aadhaar/ID value |


Note: Plain Aadhaar/ID values are never stored in the database. Only encrypted ciphertext is persisted.

Data Security & Encryption

Aadhaar/ID data is encrypted before database storage

Encryption is implemented using Fernet (AES-based symmetric encryption)

Only encrypted values are stored at rest

Decryption occurs only when returning data to authenticated users

Encryption logic was verified using Django shell and database inspection

Frontend Security UX

JWT token is stored securely in browser localStorage

Axios interceptor automatically attaches the token to API requests

Aadhaar is masked by default on the UI

Users can explicitly reveal the full Aadhaar using a password-style eye toggle

Logout clears authentication state immediately

**AI Tool Usage Log** 

AI-based development tools were used to improve productivity and correctness during development.

AI-Assisted Tasks

Assisted in designing JWT-based authentication flow

Helped generate encryption/decryption utility structure

Assisted in debugging Django configuration and environment issues

Assisted in structuring serializers and profile API logic

Provided guidance for React frontend architecture and API integration

Assisted in UI/UX refinement for secure Aadhaar display

Effectiveness Score

Score: 4 / 5

AI tools significantly reduced development time for boilerplate code and debugging.
Some manual intervention was required for environment-specific issues and UI fine-tuning, but overall productivity improved substantially.
