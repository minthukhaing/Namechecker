import requests

# Base URL
BASE_URL = "http://localhost:8000"

# Step 1: Login ဝင်ပြီး token ရယူ
def get_token(username: str, password: str):
    url = f"{BASE_URL}/token"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Login failed: {response.text}")

# Step 2: Secured API ကိုခေါ်
def myanmar_to_english(token: str, text: str):
    url = f"{BASE_URL}/myanmar_to_english"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"text": text}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.text}")
    

# Step 2: Secured API ကိုခေါ်
def parli_to_roman(token: str, text: str):
    url = f"{BASE_URL}/parli_to_roman"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"text": text}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.text}")

# Main function
if __name__ == "__main__":
    try:
        # 1. Token ရယူ
        token = get_token("admin", "nc")
        print("Token:", token)

        # 2. Text ပို့ပြီးစမ်းကြည့်
        result = myanmar_to_english(token, "မင်းသူခိုင်")
        print("Response:", result)

        result1 = parli_to_roman(token, "ဒေါက်တာနန္ဒမာလာဘိဝံသ")
        print("Response:", result1)

    except Exception as e:
        print("Error:", e)