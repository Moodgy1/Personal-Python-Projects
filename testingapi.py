import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    
    # This header is IMPORTANT. 
    # It tells the server: "I am a script, please give me JSON, not a website."
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        
        # Check if the connection was successful
        if response.status_code == 200:
            data = response.json()
            print("\n--- Here is your joke! ---")
            print(data['joke'])
            print("--------------------------\n")
        else:
            print(f"Server returned an error: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_joke()