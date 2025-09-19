import requests
from requests.auth import HTTPBasicAuth
import json
import os


# --- Jira Auth Config ---
JIRA_BASE_URL = "https://attalkiran.atlassian.net"
JIRA_PROJECT_KEY = "STF"
JIRA_EMAIL = "attal.kiran@gmail.com"
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# --- ADF Description Helper ---
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

# --- Define 5 Epics ---
epics = [
    {
        "name": "Metric Reliability",
        "summary": "Ensure correctness, consistency and accuracy of metric calculations.",
        "description": "Work focused on improving formula validation, test case reliability, and metric data consistency.",
        "labels": ["metrics", "reliability"],
        "components": ["MetricEngine", "TrendChart"]
    },
    {
        "name": "Scalable Infra",
        "summary": "Infrastructure enhancements for scaling across large datasets and services.",
        "description": "Efforts to support scale for millions of records, Redis optimization and cloud deployments.",
        "labels": ["infra", "scale"],
        "components": ["Backend", "Database"]
    },
    {
        "name": "Frontend Usability",
        "summary": "Improve frontend usability, accessibility and interaction quality.",
        "description": "Frontend UI design improvements, misalignment fixes and dynamic form components.",
        "labels": ["frontend", "ux"],
        "components": ["UI", "Frontend"]
    },
    {
        "name": "Versioning and Auditing",
        "summary": "Enhance version control and audit capabilities across the platform.",
        "description": "Add traceability and configuration versioning for better historical insight.",
        "labels": ["audit", "versioning"],
        "components": ["AuditTrail", "EventSetup"]
    },
    {
        "name": "Driver Summary Expansion",
        "summary": "Extend Driver Summary coverage for more metric types.",
        "description": "Support stock metrics and expand DS module across multiple attributes.",
        "labels": ["ds", "driver-summary"],
        "components": ["DS", "ModelEngine"]
    }
]

# --- Create Epics ---
for epic in epics:
    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": epic["summary"],
            "description": to_adf(epic["description"]),
            "labels": epic.get("labels", []),
            "components": [{"name": name} for name in epic.get("components", [])],
            "issuetype": {"name": "Epic"},
            "customfield_10011": epic["name"]  # Epic Name
        }
    }

    response = requests.post(
        f"{JIRA_BASE_URL}/rest/api/3/issue",
        headers=headers,
        auth=auth,
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        issue_key = response.json().get("key")
        print(f"✅ Created Epic: {issue_key} - {epic['name']}")
    else:
        print(f"❌ Failed to create Epic: {epic['name']}")
        print(f"Status: {response.status_code}, Response: {response.text}")
