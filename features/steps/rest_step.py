from behave import given, when, then
import requests

@given('I set the FastAPI REST API endpoint')
def step_set_api_endpoint(context):
    context.api_url = "http://localhost:8000/items/"

@when('I send a POST request to "/items/" with the following data')
def step_send_post_request(context):
    data = {row['name']: row['value'] for row in context.table}
    context.response = requests.post(context.api_url, json=data)

@then('the response should contain')
def step_check_response(context):
    expected_data = {row['key']: row['value'] for row in context.table}
    response_data = context.response.json()

    for key, value in expected_data.items():
        assert response_data[key] == value, f"Expected {key} to be {value}, but got {response_data[key]}"

@then('the response code should be {status_code:d}')
def step_check_response_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"