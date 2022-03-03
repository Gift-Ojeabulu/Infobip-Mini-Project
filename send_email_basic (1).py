import requests

"""
 * Send an email message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient email
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send email API reference: https://www.infobip.com/docs/api#channels/email/send-email
 * See Readme file for details.
"""

BASE_URL = "https://ej23g2.api.infobip.com"
API_KEY = "App a8a0491b7117dd3242a73b437cc03c88-6f95bc75-1966-4ad1-b5dc-98ac94ccf5af"

SENDER_EMAIL = "giftoscar98@selfserviceib.com"
RECIPIENT_EMAIL = "giftoscar98@gmail.com"
EMAIL_SUBJECT = "This is a sample email subject"
EMAIL_TEXT = "This is a sample email message."

formData = {
    "from": SENDER_EMAIL,
    "to": RECIPIENT_EMAIL,
    "subject": EMAIL_SUBJECT,
    "text": EMAIL_TEXT
}

all_headers = {
    "Authorization": API_KEY
}

response = requests.post(BASE_URL + "/email/2/send", files=formData, headers=all_headers)
print("Status Code: " + str(response.status_code))
print(response.json())
