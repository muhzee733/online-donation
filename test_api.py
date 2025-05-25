import requests
import json

def test_donation():
    url = "http://127.0.0.1:8000/api/donate/"
    
    # Test data
    data = {
        "donation_id": 3,
        "amount": 250.00,
        "card_number": "4111111111111111",
        "card_expiry": "12/26",
        "card_cvc": "123",
        "donor_name": "Ali Khan",
        "donor_email": "ali@example.com"
    }
    
    # Headers
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        # Make POST request
        response = requests.post(url, json=data, headers=headers)
        
        # Print response
        print("Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    test_donation() 