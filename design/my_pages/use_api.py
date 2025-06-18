import streamlit as st

def show():
    st.title("Use API")
    st.divider()

    with st.expander("Myanmar to English Converter API Keys"):

        with st.container():
            st.subheader("Myanmar to English Converter API")
            st.divider()
            st.write("$username = admin")
            st.write("$password = nc")
            st.write("$end-point = http:\\localhost:8000\myanmar_to_english")
            code="""
                def fun():
                    print("hello")

            """
            st.code(code,language="python",line_numbers=True,wrap_lines=True,)
    
    with st.expander("Parli to Roman Converter API Keys"):

        with st.container():
            st.subheader("Parli to Roman Converter API Keys")
            st.divider()
            st.write("$username = admin")
            st.write("$password = nc")
            st.write("$end-point = http:\\localhost:8000\myanmar_to_english")
            code="""
                def fun():
                    print("hello")

            """
            st.code(code,language="python",line_numbers=True,wrap_lines=True,)

    st.title("How to use API with any language")

    with st.expander("CURL"):

        with st.container():
            st.subheader("How to call curl language (bash)")
            st.divider()
            st.write("✅ Step 1: Token ရယူခြင်း (/token)")
            code="""
                curl -X POST "http://localhost:8000/token" \
                -H "Content-Type: application/x-www-form-urlencoded" \
                -d "username=admin&password=nc"
            """
            st.code(code,language="bash",line_numbers=True,wrap_lines=True,)
            st.write("📌 Output (နမူနာ):")
            code="""
                {
                    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx",
                    "token_type": "bearer"
                }
            """
            st.code(code,language="json",line_numbers=True,wrap_lines=True,)

            st.write("✅ Step 2: /myanmar_to_english ခေါ်နည်း")
            code="""
                curl -X POST "http://localhost:8000/myanmar_to_english" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx" \
     -H "Content-Type: application/json" \
     -d '{"text":"မင်းသူခိုင်"}'
            """
            st.code(code,language="bash",line_numbers=True,wrap_lines=True,)

            st.write("✅ Step 3: /parli_to_roman ခေါ်နည်း")
            code="""
                {
                    "received_text": "Converted by myan: မင်းသူခိုင်",
                    "length": 7,
                    "message": "Thank you for the text(myanmar_to_english): 'Minn Thuu Khaing'",
                    "user": "admin"
                }
            """
            st.code(code,language="json",line_numbers=True,wrap_lines=True,)

    with st.expander("Python Language"):

        with st.container():
            st.subheader("How to call python language")
            st.divider()
            st.write("✅ python မှာ အရင်ဆုံး ဒါကို install လုပ်ပါ")
           
            code="""
                pip install request
            """
            st.code(code,language="bash",line_numbers=True,wrap_lines=True,)
            st.write("✅ ဒါကို copy ယူပြီး အသုံးပြုနိုင်ပါတယ်")
           
            code="""
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

            """
            st.code(code,language="python",line_numbers=True,wrap_lines=True,)

    with st.expander("PHP Language"):

        with st.container():
            st.subheader("How to call php language")
            st.divider()
            st.write("✅ ဒါကို copy ယူပြီး အသုံးပြုနိုင်ပါတယ်")
           
            code="""
                <?php

                $BASE_URL = "http://localhost:8000";

                // Step 1: Login ဝင်ပြီး token ရယူ
                function get_token($username, $password) {
                    global $BASE_URL;

                    $url = $BASE_URL . "/token";
                    $data = [
                        'username' => $username,
                        'password' => $password
                    ];

                    $ch = curl_init($url);
                    curl_setopt($ch, CURLOPT_POST, true);
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                    curl_setopt($ch, CURLOPT_HEADER, false);

                    $response = curl_exec($ch);
                    if ($response === FALSE) {
                        die('Curl error: ' . curl_error($ch));
                    }

                    curl_close($ch);
                    $json = json_decode($response, true);

                    if (isset($json['access_token'])) {
                        return $json['access_token'];
                    } else {
                        throw new Exception("Login failed: " . $response);
                    }
                }

                // Step 2: myanmar_to_english endpoint ကိုခေါ်
                function myanmar_to_english($token, $text) {
                    global $BASE_URL;

                    $url = $BASE_URL . "/myanmar_to_english";
                    return send_post_request($url, $token, $text);
                }

                // Step 2: parli_to_roman endpoint ကိုခေါ်
                function parli_to_roman($token, $text) {
                    global $BASE_URL;

                    $url = $BASE_URL . "/parli_to_roman";
                    return send_post_request($url, $token, $text);
                }

                // Helper function for sending POST requests
                function send_post_request($url, $token, $text) {
                    $payload = json_encode(['text' => $text]);

                    $ch = curl_init($url);
                    curl_setopt($ch, CURLOPT_POST, true);
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                    curl_setopt($ch, CURLOPT_HTTPHEADER, [
                        "Authorization: Bearer $token",
                        "Content-Type: application/json"
                    ]);

                    $response = curl_exec($ch);
                    if ($response === FALSE) {
                        die('Curl error: ' . curl_error($ch));
                    }

                    curl_close($ch);
                    return json_decode($response, true);
                }

                // Main execution
                try {
                    // 1. Token ရယူ
                    $token = get_token("admin", "nc");
                    echo "Token: " . $token . "\n\n";

                    // 2. myanmar_to_english စမ်းကြည့်
                    $result = myanmar_to_english($token, "မင်းသူခိုင်");
                    echo "Myanmar to English Response:\n";
                    print_r($result);

                    // 3. parli_to_roman စမ်းကြည့်
                    $result1 = parli_to_roman($token, "ဒေါက်တာနန္ဒမာလာဘိဝံသ");
                    echo "\nParli to Roman Response:\n";
                    print_r($result1);

                } catch (Exception $e) {
                    echo "Error: " . $e->getMessage() . "\n";
                }

                ?>

            """
            st.code(code,language="php",line_numbers=True,wrap_lines=True,)

    with st.expander("NodeJS Language"):

        with st.container():
            st.subheader("How to call nodejs language")
            st.divider()
            st.write("✅ Node.js Version (Axios သုံးထားပါတယ်)")
           
            code="""
                npm install axios
            """
            st.code(code,language="bash",line_numbers=True,wrap_lines=True,)

            st.write("✅ ဒါကို copy ယူပြီး အသုံးပြုနိုင်ပါတယ်")

            code="""
                const axios = require('axios');

                const BASE_URL = "http://localhost:8000";

                // Step 1: Login ဝင်ပြီး token ရယူ
                async function get_token(username, password) {
                    try {
                        const response = await axios.post(`${BASE_URL}/token`, 
                            new URLSearchParams({
                                username,
                                password
                            }).toString(),
                            {
                                headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'
                                }
                            }
                        );
                        return response.data.access_token;
                    } catch (error) {
                        throw new Error(`Login failed: ${error.response?.data || error.message}`);
                    }
                }

                // Step 2: myanmar_to_english endpoint ကိုခေါ်
                async function myanmar_to_english(token, text) {
                    try {
                        const response = await axios.post(`${BASE_URL}/myanmar_to_english`, 
                            { text },
                            {
                                headers: {
                                    'Authorization': `Bearer ${token}`,
                                    'Content-Type': 'application/json'
                                }
                            }
                        );
                        return response.data;
                    } catch (error) {
                        throw new Error(`Request failed: ${error.response?.data || error.message}`);
                    }
                }

                // Step 2: parli_to_roman endpoint ကိုခေါ်
                async function parli_to_roman(token, text) {
                    try {
                        const response = await axios.post(`${BASE_URL}/parli_to_roman`, 
                            { text },
                            {
                                headers: {
                                    'Authorization': `Bearer ${token}`,
                                    'Content-Type': 'application/json'
                                }
                            }
                        );
                        return response.data;
                    } catch (error) {
                        throw new Error(`Request failed: ${error.response?.data || error.message}`);
                    }
                }

                // Main function
                (async () => {
                    try {
                        // 1. Token ရယူ
                        const token = await get_token("admin", "nc");
                        console.log("Token:", token);

                        // 2. Myanmar to English စမ်းကြည့်
                        const result = await myanmar_to_english(token, "မင်းသူခိုင်");
                        console.log("Myanmar to English Response:", result);

                        // 3. Pali to Roman စမ်းကြည့်
                        const result1 = await parli_to_roman(token, "ဒေါက်တာနန္ဒမာလာဘိဝံသ");
                        console.log("Parli to Roman Response:", result1);

                    } catch (error) {
                        console.error("Error:", error.message);
                    }
                })();

            """
            st.code(code,language="nodejs",line_numbers=True,wrap_lines=True,)