from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "kesar123"

@app.post("/honeypot")
def honeypot(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "scam_detected": True,
        "scam_type": "UPI Fraud",
        "extracted_data": {
            "upi_id": "fraud@upi",
            "bank_account": "XXXXXX1234",
            "phishing_link": "http://fake-link.com"
        },
        "message": "Scam interaction handled successfully"
    }
