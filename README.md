# Advanced AI Demand Forecasting Enhancements

## Project Overview

The Advanced AI Demand Forecasting System is a full-stack web application developed using FastAPI, React.js, SQLAlchemy, JWT Authentication, Pandas, and Machine Learning models.

The system is designed to:
- Upload historical sales datasets
- Preprocess data
- Generate future demand forecasting
- Display analytics dashboards
- Export PDF and Excel reports
- Manage notifications and admin operations

---

# Technologies Used

## Backend
- FastAPI
- SQLAlchemy
- JWT Authentication
- Pandas
- Scikit-learn
- Prophet
- PostgreSQL / MySQL

## Frontend
- React.js
- Tailwind CSS
- Axios
- Recharts
- Vite

---

# Features

## Authentication Module
- User Registration
- User Login
- JWT Token Authentication
- Protected APIs

## Dataset Module
- Upload CSV/Excel Files
- Validate Dataset
- Handle Missing Values
- Delete Dataset
- Search Dataset
- List User Datasets

## Forecasting Module
- Data Preprocessing
- Forecast Generation
- Forecast Accuracy Metrics
- Forecast History

## Dashboard & Analytics
- Total Sales
- Monthly Sales Trends
- Forecast Accuracy
- Top Products
- Analytics Charts

## Reports Module
- Generate PDF Reports
- Export Excel Reports
- Download Reports

## Notifications Module
- In-App Notifications
- Mark Notification as Read
- Mark All Notifications as Read

## Admin Module
- List Users
- Delete Users
- List All Datasets
- List All Forecasts
- Monitor Activities

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend Server

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Install Frontend Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# API Endpoints

## Authentication APIs

- POST /auth/register
- POST /auth/login

## Dataset APIs

- POST /datasets/upload
- GET /datasets/list
- GET /datasets/search
- DELETE /datasets/purge

## Forecast APIs

- POST /forecast/preprocess
- POST /forecast/generate

## Report APIs

- GET /reports/export/pdf
- GET /reports/export/excel

## Notification APIs

- GET /notifications
- PUT /notifications/read/{id}
- PUT /notifications/read-all

## Admin APIs

- GET /admin/users
- DELETE /admin/user/{id}
- GET /admin/datasets
- GET /admin/forecasts
- GET /admin/activities

---

# Output

The application provides:
- AI-based Demand Forecasting
- Interactive Dashboard
- Analytics Charts
- Export Reports
- Notification Management
- Admin Dashboard

---

# Conclusion

The Advanced AI Demand Forecasting System helps businesses analyze historical sales data and predict future demand using AI and Machine Learning models. The application also provides dashboard analytics, report exporting, notifications, and admin management functionalities.
