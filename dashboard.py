import requests
import json

# set the API endpoint and keys
api_url = 'https://api.datadoghq.com/api/v1/dashboard'
api_key = 'fbcfe4ec565ecd905780c1d9fded3121'
app_key = '9b07792484ddf34f927eec3ac2e5aeb7605d8915'

# set the dashboard name
dashboard_name = '2.create dashboard'

# construct the API headers
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key,
}

# make the API request to list all dashboards
response = requests.get(api_url, headers=headers)

# parse the response JSON
dashboards = json.loads(response.content)

# find the ID of the specified dashboard
dashboard_id = None
for dashboard in dashboards:
    if dashboard['title'] == dashboard_name:
        dashboard_id = dashboard['id']
        break

# print the ID of the specified dashboard
if dashboard_id is None:
    print("Dashboard '{}' not found.".format(dashboard_name))
else:
    print("The ID of the '{}' dashboard is: {}".format(dashboard_name, dashboard_id))

