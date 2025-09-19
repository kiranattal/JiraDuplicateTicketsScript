import requests
from requests.auth import HTTPBasicAuth
import json
from jiraticketduplicate import tickets
import os
# --- Jira Auth Config ---
JIRA_BASE_URL = "https://attalkiran.atlassian.net"   # <--- Replace this
JIRA_PROJECT_KEY = "STF"                              # <--- Replace this
JIRA_EMAIL = "attal.kiran@gmail.com"                  # <--- Replace this
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# --- ADF Format Helper ---
def to_adf(description_text):
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": description_text
                    }
                ]
            }
        ]
    }


def create_ticket(ticket):
    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": ticket["summary"],
            "description": to_adf(ticket["description"]),
            "labels": ticket.get("labels", []),
            "components": [{"name": comp} for comp in ticket.get("components", [])],
            "issuetype": {"name": ticket["issuetype"]},
            "customfield_10014": ticket["epic"]  # Epic Link
        }
    }

    response = requests.post(f"{JIRA_BASE_URL}/rest/api/3/issue", headers=headers, auth=auth, data=json.dumps(payload))
    if response.status_code == 201:
        print(f" Created ticket: {response.json().get('key')} - {ticket['summary']}")
    else:
        print(f" Failed to create ticket: {ticket['summary']} => {response.text}")

for ticket in tickets:
    #print(ticket["summary"])
    create_ticket(ticket)

