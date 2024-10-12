
# StockClock - FastAPI CRUD Application

**StockClock** is a simple CRUD (Create, Read, Update, Delete) application built with **FastAPI** and **MongoDB**. It supports two primary entities:
- **Items**: Manages inventory items with attributes like `name`, `email`, `item_name`, `quantity`, and `expiry_date`.
- **Clock-In Records**: Handles user clock-in records, storing `email`, `location`, and the time of clock-in.

The project demonstrates best practices for organizing FastAPI applications by separating routes and controllers.

## Features
- Full CRUD operations for both **Items** and **Clock-In Records**.
- Flexible filtering options for both entities.
- Aggregation for Items, grouping data by `email`.
- MongoDB as the primary database.
- Swagger documentation for easy API testing.

## Project Structure

```
StockClock/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Main entry point for the FastAPI application
│   ├── models/                # Pydantic models for data validation
│   │   ├── item_model.py
│   │   ├── clock_in_model.py
│   ├── routes/                # API route definitions
│   │   ├── item_routes.py
│   │   ├── clock_in_routes.py
│   ├── controllers/           # Controller functions handling business logic
│   │   ├── item_controller.py
│   │   ├── clock_in_controller.py
│   ├── database/              # Database connection setup
│   │   ├── connection.py
├── README.md
├── requirements.txt           # Dependencies for the project
```

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **MongoDB** (locally or using MongoDB Atlas)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd StockClock
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API documentation**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the Swagger UI.

## API Documentation

### 1. **Items API**

| Endpoint               | Method | Description                                      |
|------------------------|--------|--------------------------------------------------|
| `/items/`              | POST   | Create a new item                                |
| `/items/{item_id}`      | GET    | Retrieve a specific item by its ID               |
| `/items/filter`         | GET    | Filter items based on query parameters           |
| `/items/aggregate`      | GET    | Aggregate items by `email`, return count per user|
| `/items/{item_id}`      | DELETE | Delete an item by its ID                         |
| `/items/{item_id}`      | PUT    | Update an item’s details by its ID               |

#### Example Item JSON:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "item_name": "Laptop",
  "quantity": 2,
  "expiry_date": "2025-01-01"
}
```

### 2. **Clock-In Records API**

| Endpoint                 | Method | Description                                      |
|--------------------------|--------|--------------------------------------------------|
| `/clock-in/`              | POST   | Create a new clock-in record                     |
| `/clock-in/{clock_in_id}` | GET    | Retrieve a specific clock-in record by its ID    |
| `/clock-in/filter`        | GET    | Filter clock-in records based on query parameters|
| `/clock-in/{clock_in_id}` | DELETE | Delete a clock-in record by its ID               |
| `/clock-in/{clock_in_id}` | PUT    | Update a clock-in record by its ID               |

#### Example Clock-In JSON:
```json
{
  "email": "john@example.com",
  "location": "Office"
}
```

## Filtering API Endpoints

### Items Filter Parameters:
- `email`: Filter by user email.
- `expiry_date`: Items expiring after a specific date.
- `insert_date`: Items inserted after a specific date.
- `quantity`: Items with quantity greater than or equal to the provided value.

Example:
```http
GET /items/filter?email=john@example.com&quantity=2
```

### Clock-In Records Filter Parameters:
- `email`: Filter by user email.
- `location`: Filter by clock-in location.
- `insert_date`: Filter records inserted after a specific date.

Example:
```http
GET /clock-in/filter?email=john@example.com&location=Office
```
