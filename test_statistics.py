import requests
import json

def test_statistics():
    url = "http://127.0.0.1:8000/api/platforms/statistics/"
    
    try:
        # Make GET request
        response = requests.get(url)
        
        # Print response
        print("Status Code:", response.status_code)
        print("Response:", json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    test_statistics() 