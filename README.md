# HRMS – Human Resource Management System

A lightweight Human Resource Management System built with **FastAPI** and **React**.
The application provides a simple interface to manage employees, track attendance, and view basic HR metrics.

The project is structured as a **separate frontend and backend**, with the backend deployed on Render and the frontend hosted on Netlify.

## Live Application

Frontend
https://hrmssolanki.netlify.app

Backend API
https://hrms-backend-q1re.onrender.com

API Documentation
https://hrms-backend-q1re.onrender.com/docs
## Tech Stack

Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn

Frontend

* React
* Axios

Deployment

* Render (Backend + PostgreSQL)
* Netlify (Frontend)

---

## Project Structure

Backend

hrms-backend
│
├── app
│   ├── api
│   │   ├── employee.py
│   │   ├── attendance.py
│   │   └── dashboard.py
│   │
│   ├── database
│   │   └── postgres.py
│   │
│   ├── models
│   │   ├── base_model.py
│   │   ├── employee_model.py
│   │   └── attendance_model.py
│   │
│   └── main.py
│
└── requirements.txt

Frontend
hrms-frontend
│
├── src
│   ├── components
│   ├── pages
│   ├── api.js
│   └── App.js
│
└── package.json

## Features

* Employee management
* Attendance tracking
* Basic HR dashboard
* REST API with FastAPI
* PostgreSQL persistence

## Running the Backend

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

The API will be available at:

http://localhost:8000

Interactive documentation:

http://localhost:8000/docs

## Database Configuration

The application expects a PostgreSQL connection string in the environment variable:

DATABASE_URL

Example:

postgresql://postgres:password@localhost:5432/hrms


## Running the Frontend

Install dependencies:

npm install

Start the development server:

npm start

Application will run at:

http://localhost:3000


## API Configuration

Frontend requests are configured through Axios.

`src/api.js`

import axios from "axios";

const API = axios.create({
  baseURL: "https://hrms-backend-q1re.onrender.com"
});

export default API;


## Deployment

Backend is deployed on **Render** using a connected GitHub repository.

Start command:

uvicorn app.main:app --host 0.0.0.0 --port 8000

Frontend is deployed on **Netlify** with:

Build command: npm run build
Publish directory: build
