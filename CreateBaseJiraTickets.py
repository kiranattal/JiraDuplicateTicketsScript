import requests
from requests.auth import HTTPBasicAuth
import json
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

# --- Epics ---
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

# --- Tickets ---
tickets = [
    {"summary": "Fix TC failures for %Active Metric in Trend Chart", "description": "Test cases for the %Active Metric Trend Chart are failing due to formula inconsistencies. Requires investigation and fix.", "labels": ["metric-type", "tc-failure"], "components": ["TrendChart"], "issuetype": "Bug", "epic": "Metric Reliability"},
    {"summary": "Create stock and %active metrics from frontend UI", "description": "Allow users to create new stock and %active metrics directly from the frontend interface during event creation.", "labels": ["frontend", "metric-creation"], "components": ["UI"], "issuetype": "Story", "epic": "Frontend Usability"},
    {"summary": "MySQL support for MetricUploader during regression", "description": "Add MySQL support to MetricUploader module for proper data handling during regression testing cycles.", "labels": ["mysql", "backend"], "components": ["Database"], "issuetype": "Task", "epic": "Scalable Infra"},
    {"summary": "Integrate Redis caching into output data fetch", "description": "Introduce Redis caching to reduce backend load when fetching large output datasets.", "labels": ["redis", "performance"], "components": ["Backend"], "issuetype": "Story", "epic": "Scalable Infra"},
    {"summary": "Optimizing performance on RG, DS, TC, CG, GVA by refactoring code", "description": "The RG (Result Grid), DS (Driver Summary), TC (Trendchart), CG (compare groups), and GVA (Group Value Attribute) modules are experiencing slowness. Refactor the underlying logic and structure to enhance runtime performance and responsiveness.", "labels": ["trendchart", "metric-logic","performance","optimziation"], "components": ["MetricEngine"], "issuetype": "Bug", "epic": "Metric Reliability"},
    {"summary": "Create UI for Event Setup Metric Selection", "description": "Develop frontend UI to allow metric and attribute selection during event setup.", "labels": ["ui", "event-setup"], "components": ["Frontend"], "issuetype": "Story", "epic": "Frontend Usability"},
    {"summary": "Set up SEQ testing environment for Redis integration", "description": "Provision SEQ environment to test Redis caching performance and verify feature compatibility.", "labels": ["seq", "redis"], "components": ["CacheLayer"], "issuetype": "Task", "epic": "Scalable Infra"},
    {"summary": "Add versioning to analysis settings inside event", "description": "Support multiple analysis settings within a single event, each producing independent outputs.", "labels": ["analysis", "versioning"], "components": ["Versioning"], "issuetype": "Story", "epic": "Versioning and Auditing"},
    {"summary": "Enable role-based permissions to access events", "description": "Implement fine-grained access control for events based on user roles. Users should only be able to view, edit, or delete events depending on their assigned role (e.g., viewer, editor, admin). This includes enforcing backend-level checks and updating the UI accordingly to reflect restricted actions.", "labels": ["event", "permissions"], "components": ["EventSetup"], "issuetype": "Task", "epic": "Versioning and Auditing"},
    {"summary": "Resolve GVA misalignment issue on group screen", "description": "Group Value Attribute (GVA) screen shows layout misalignment in Chrome and Firefox browsers.", "labels": ["gva", "ux"], "components": ["UX"], "issuetype": "Bug", "epic": "Frontend Usability"},

    {"summary": "Develop DS module for stock metric", "description": "Implement Driver Summary for stock metrics across all event types and validate outputs.", "labels": ["ds", "stock-metric"], "components": ["DS"], "issuetype": "Task", "epic": "Driver Summary Expansion"},
    {"summary": "Optimize model summary computation performance", "description": "Model summary computation is slow for large datasets. Requires algorithm optimization and code refactoring.", "labels": ["model-summary", "performance"], "components": ["ModelEngine"], "issuetype": "Task", "epic": "Driver Summary Expansion"},
    {"summary": "Fix deadlock caused by multiprocessing in CG", "description": "Deadlocks occur during concurrent execution of CG module. Identify and fix multiprocessing root cause.", "labels": ["deadlock", "multiprocessing"], "components": ["CG"], "issuetype": "Bug", "epic": "Scalable Infra"},
    {"summary": "Fix model application timeout during adhoc upload", "description": "Model application fails with timeout errors during adhoc data upload. Needs fix and retry logic.", "labels": ["model", "timeout"], "components": ["Upload"], "issuetype": "Bug", "epic": "Driver Summary Expansion"},
    {"summary": "Restrict access to Event header edit for private users", "description": "Permissioning module should block private users from editing event headers.", "labels": ["permissioning", "security"], "components": ["UserAccess"], "issuetype": "Bug", "epic": "Versioning and Auditing"},
    {"summary": "Set up centralized database for transactions, attributes, metrics and separate outputs DB", "description": "Design and implement a centralized relational database to store all transactions, customer attributes, and metric configurations. A separate optimized outputs database will store result datasets generated during processing. Ensure clear schema separation, indexing for performance, and scalability for future integrations.", "labels": ["database", "architecture"], "components": ["MetricEngine"], "issuetype": "Story", "epic": "Scalable Infra"},
    {"summary": "Containerize Task Server for deployment on Linux VMs", "description": "Containerize the task server to support deployments on Linux-based VMs for better portability and scalability.", "labels": ["containerization", "linux"], "components": ["Deployment"], "issuetype": "Task", "epic": "Scalable Infra"},
    {"summary": "Build result grid for segmentation outputs", "description": "Create result grid to show segmentation output grouped by customer dimensions.", "labels": ["segmentation", "result-grid"], "components": ["ResultGrid"], "issuetype": "Story", "epic": "Frontend Usability"},
    {"summary": "Create attribute upload feature from frontend", "description": "Enable creation of new customer attributes directly from frontend with validations.", "labels": ["attribute", "upload"], "components": ["AttributeUploader"], "issuetype": "Story", "epic": "Frontend Usability"},
    {"summary": "Scale MySQL database for 4M customer records", "description": "Optimize schema and query strategy to support 4M customer records in MySQL database for CMB use case.", "labels": ["scalability", "mysql"], "components": ["Performance"], "issuetype": "Task", "epic": "Scalable Infra"}
]

# --- Script Functions ---

def create_epics():
    epic_name_to_key = {}
    for epic in epics:
        payload = {
            "fields": {
                "project": {"key": JIRA_PROJECT_KEY},
                "summary": epic["summary"],
                "description": to_adf(epic["description"]),
                "labels": epic.get("labels", []),
                "components": [{"name": comp} for comp in epic.get("components", [])],
                "issuetype": {"name": "Epic"},
                "customfield_10011": epic["name"]  # Epic Name
            }
        }

        response = requests.post(f"{JIRA_BASE_URL}/rest/api/3/issue", headers=headers, auth=auth, data=json.dumps(payload))
        if response.status_code == 201:
            key = response.json().get("key")
            epic_name_to_key[epic["name"]] = key
            print(f"✅ Created Epic: {key} - {epic['name']}")
        else:
            print(f"❌ Failed to create epic: {epic['name']} => {response.text}")
    return epic_name_to_key

def create_ticket(ticket, epic_map):
    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": ticket["summary"],
            "description": to_adf(ticket["description"]),
            "labels": ticket.get("labels", []),
            "components": [{"name": comp} for comp in ticket.get("components", [])],
            "issuetype": {"name": ticket["issuetype"]},
            "customfield_10014": epic_map.get(ticket["epic"])  # Epic Link
        }
    }

    response = requests.post(f"{JIRA_BASE_URL}/rest/api/3/issue", headers=headers, auth=auth, data=json.dumps(payload))
    if response.status_code == 201:
        print(f"✅ Created ticket: {response.json().get('key')} - {ticket['summary']}")
    else:
        print(f"❌ Failed to create ticket: {ticket['summary']} => {response.text}")

# --- Execution ---
epic_map = create_epics()
for ticket in tickets:
    create_ticket(ticket, epic_map)
    print("Added base ticket successfully..")
