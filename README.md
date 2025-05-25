# Donation Platform API Documentation

This API provides endpoints for managing donations and donation platforms. Below are the detailed descriptions of all available endpoints.

## Base URL
```
http://127.0.0.1:8000/api/
```

## Endpoints

### 1. Donation Statistics
Get overall donation statistics and detailed donation records.

**Endpoint:** `GET /platforms/statistics/`

**Response:**
```json
{
  "overall_statistics": {
    "total_donations": 2,
    "total_amount": 500.0,
    "unique_donors": 1
  },
  "donation_records": [
    {
      "id": 2,
      "amount": 250.0,
      "donor_name": "Ali Khan",
      "donor_email": "ali@example.com",
      "card_number": "1111",
      "card_expiry": "12/26",
      "status": "success",
      "created_at": "2025-05-25T13:28:49.331466Z",
      "platform__name": "Beit Al Khair Society",
      "platform__id": 4
    }
  ]
}
```

### 2. Make a Donation
Submit a new donation.

**Endpoint:** `POST /donate/`

**Request Body:**
```json
{
  "donation_id": 3,
  "amount": 250.00,
  "card_number": "4111111111111111",
  "card_expiry": "12/26",
  "card_cvc": "123",
  "donor_name": "Ali Khan",
  "donor_email": "ali@example.com"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Donation processed successfully",
  "data": {
    "donation_id": 3,
    "amount": 250.0,
    "donor_name": "Ali Khan"
  }
}
```

### 3. List Donation Platforms
Get all available donation platforms.

**Endpoint:** `GET /platforms/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Dubai Cares",
    "description": "Description of Dubai Cares",
    "website": "https://www.dubaicares.ae",
    "logo_url": "https://example.com/logo.png",
    "location": "Dubai, UAE",
    "contact_email": "contact@dubaicares.ae",
    "phone": "+971-4-1234567"
  }
]
```

### 4. Get Single Platform
Get details of a specific donation platform.

**Endpoint:** `GET /platforms/{id}/`

**Response:**
```json
{
  "id": 1,
  "name": "Dubai Cares",
  "description": "Description of Dubai Cares",
  "website": "https://www.dubaicares.ae",
  "logo_url": "https://example.com/logo.png",
  "location": "Dubai, UAE",
  "contact_email": "contact@dubaicares.ae",
  "phone": "+971-4-1234567"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid input data"
}
```

### 404 Not Found
```json
{
  "error": "Donation platform not found"
}
```

### 405 Method Not Allowed
```json
{
  "detail": "Method 'GET' not allowed."
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error message"
}
```

## Testing the API

### Using Python Requests
```python
import requests
import json

# Test donation endpoint
def test_donation():
    url = "http://127.0.0.1:8000/api/donate/"
    data = {
        "donation_id": 3,
        "amount": 250.00,
        "card_number": "4111111111111111",
        "card_expiry": "12/26",
        "card_cvc": "123",
        "donor_name": "Ali Khan",
        "donor_email": "ali@example.com"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    print(response.json())

# Test statistics endpoint
def test_statistics():
    url = "http://127.0.0.1:8000/api/platforms/statistics/"
    response = requests.get(url)
    print(response.json())
```

### Using cURL
```bash
# Get statistics
curl -X GET http://127.0.0.1:8000/api/platforms/statistics/

# Make a donation
curl -X POST http://127.0.0.1:8000/api/donate/ \
  -H "Content-Type: application/json" \
  -d '{
    "donation_id": 3,
    "amount": 250.00,
    "card_number": "4111111111111111",
    "card_expiry": "12/26",
    "card_cvc": "123",
    "donor_name": "Ali Khan",
    "donor_email": "ali@example.com"
  }'
```

## Security Notes
1. Card numbers are stored with only the last 4 digits
2. CORS is enabled for all origins
3. CSRF protection is disabled for the donation endpoint
4. All amounts are stored as decimal values

## Setup and Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the server:
```bash
python manage.py runserver
```

## Dependencies
- Django
- Django REST Framework
- django-cors-headers
- requests (for testing) 