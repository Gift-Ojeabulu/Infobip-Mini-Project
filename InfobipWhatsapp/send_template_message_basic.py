import requests

"""
 * Send WhatsApp template message directly by calling HTTP endpoint.
 *
 *
 * Send WhatsApp API reference: https://www.infobip.com/docs/api#channels/whatsapp/send-whatsapp-template-message
 *
 
"""

BASE_URL = "https://ej23g2.api.infobip.com"
API_KEY = "App a8a0491b7117dd3242a73b437cc03c88-6f95bc75-1966-4ad1-b5dc-98ac94ccf5af"

SENDER = "447860099299"
RECIPIENT = "2349077393129"

payload = {
    "messages":
        [
            {
                "from": SENDER,
                "to": RECIPIENT,
                "content": {
                    "templateName": "registration_success",
                    "templateData": {
                      "body": {
                        "placeholders": [
                          "sender",
                          "message",
                          "delivered",
                          "testing"
                        ]
                      },
                      "header": {
                        "type": "IMAGE",
                        "mediaUrl": "https://api.infobip.com/ott/1/media/infobipLogo"
                      },
                      "buttons": [
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "yes-payload"
                        },
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "no-payload"
                        },
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "later-payload"
                        }
                      ]
                  },
                  "language": "en"
               }
           }
        ]
    }

headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(BASE_URL + "/whatsapp/1/message/template", json=payload, headers=headers)

print(response.json())
