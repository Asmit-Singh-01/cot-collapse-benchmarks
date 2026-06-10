import os
import http.client
import json

def test_ai_logic():
    # GitHub Secrets se key uthana
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[!] Execution Failed: API Key missing in environment secrets.")
        return

    print("[*] Accessing Google AI Studio Server...")
    
    # Google Gemini Flash Model Endpoint connect karna
    host = "generativelanguage.googleapis.com"
    url = f"/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    
    # AI ko ghumane waala reasoning puzzle test request
    payload = {
        "contents": [{
            "parts": [{
                "text": "Solve step-by-step: A box has 3 red apples. I remove 2 red apples and add 2 green apples. Then I paint 1 red apple black. How many red apples are left in total? Explain each step of your thought process."
            }]
        }]
    }

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", url, body=json.dumps(payload), headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        
        result = json.loads(data)
        # Full logic sequence dump karna screen par
        ai_reply = result['candidates'][0]['content']['parts'][0]['text']
        
        print("\n--- [ LIVE AI CHAIN-OF-THOUGHT LOGIC REPORT ] ---")
        print(ai_reply)
        print("--------------------------------------------------")
        print("[+] Success: Evaluation pipeline closed with 0 errors.")
        
    except Exception as e:
        print(f"[!] Engine Error during logical parsing: {str(e)}")

if __name__ == "__main__":
    test_ai_logic()
  
