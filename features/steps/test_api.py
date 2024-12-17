from behave import given, when, then
import requests

@given('I set the API endpoint "{endpoint}"')
def step_set_api_endpoint(context, endpoint):
    context.api_url = f"http://localhost:8000{endpoint}"

@when("I send a GET request")
def step_send_get_request(context):
    context.response = requests.get(context.api_url)

@then('the response should contain "{message}"')
def step_check_response_content(context, message):
    response_data = context.response.json()
    assert response_data['message'] == message, f"Expected {message}, got {response_data['message']}"

@then("the response code should be {status_code:d}")
def step_check_response_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"