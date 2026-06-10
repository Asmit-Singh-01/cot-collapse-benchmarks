import os
import http.client
import json

def test_groq_ai_logic():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("[!] Execution Failed: GROQ_API_KEY missing in environment secrets.")
        return

    print("[*] Accessing Groq Ultra-Fast AI Server...")
    
    host = "api.groq.com"
    url = "/openai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Yahan naya active model use kiya hai
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user",
                "content": "Solve step-by-step: A box has 3 red apples. I remove 2 red apples and add 2 green apples. Then I paint 1 red apple black. How many red apples are left in total?"
            }
        ]
    }

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", url, body=json.dumps(payload), headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        
        result = json.loads(data)
        
        if 'error' in result:
            print("\n[!] SERVER RETURNED AN ERROR:")
            print(json.dumps(result['error'], indent=2))
            return

        ai_reply = result['choices'][0]['message']['content']
        print("\n--- [ LIVE GROQ AI CHAIN-OF-THOUGHT LOGIC REPORT ] ---")
        print(ai_reply)
        print("--------------------------------------------------")
        
    except Exception as e:
        print(f"[!] Engine Error during parsing: {str(e)}")

if __name__ == "__main__":
    test_groq_ai_logic()
    
