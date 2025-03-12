import requests
# from content_input_template import get_filled_prompt_template
import os

apikey = os.environ.get("N8NAPI")

fields = {
    'topic': "Appellate Law in Indiana: A Comprehensive Overview of the Appeals Process and when to hire an attorney",
    'client_name': "Ciyou & Associates",
    'client_url': "https://ciyoulaw.com",
    'client_logo_url': "https://ciyoulaw.com/wp-content/uploads/2022/11/Ciyou-Associates-Logo-Outlined.jpg",
    'client_contact_info': "+1 (317) 210-2000",
    'tone': "authoritative yet approachable",
    'style': "professional but not overly technical",
    'expertise_level': "expert in appellate law demonstrating deep knowledge",
    'client_positioning': "trusted advisor in complex legal matters",
    'target_audience': "people facing a final court order that aren’t happy with the outcome and want to know what their options are for an appeal",
    'core_topics': [
        "Introduction to Indiana Appellate Law",
        "What is the Appeals Process in Indiana?",
        "Filing an Appeal in Indiana: Step-by-Step Guide",
        "Indiana Family Law Appeals: Common Scenarios",
        "Understanding the Role of the Appellate Court in Indiana",
        "Deadlines and Requirements for Appeals in Indiana",
        "The Appeals Brief: How to Craft a Persuasive Argument",
        "Common Outcomes in Indiana Appeals",
        "Case Studies: Successful Appeals in Indiana",
        "Tips for Navigating the Appeals Process in Indiana",
    ],
    "recipient_email": "samuel@coherentautomation.com",
}

# filled_prompt = get_filled_prompt_template(**fields)
headers = {"Content-Type": "application/json",
           "Authorization": f"token {apikey}"}

api_base_url = "http://localhost:5678/webhook-test/"
api_endpoint = "66edbec3-dee4-402b-b36c-11fd270265ff"
api_url = f"http://localhost:5678/webhook-test/{api_endpoint}"

res = requests.post(
    api_url,
    json=fields, headers=headers)

"""
# n8n pyodide code:
form_input = _input.all().to_py()[0]
data = form_input["json"]["body"]

template = "some stuff"

return [{"prompt": template}]
"""

print(res)
