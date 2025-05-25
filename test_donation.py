import requests

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
    
    try:
        response = requests.post(url, json=data)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    test_donation() 