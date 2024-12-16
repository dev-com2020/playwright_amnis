from behave import given, when, then

@given('istnieje kolejka SQS')
def step_impl(context):
    assert hasattr(context, 'queue_url'), "Kolejka nie została utworzona"
    assert context.queue_url is not None, "Kolejka nie została utworzona"

@when('wysyłam wiadomość "{message}"')
def step_impl(context, message):
    response = context.sqs.send_message(
        QueueUrl=context.queue_url,
        MessageBody=message
    )
    assert 'MessageId' in response, "Wiadomość nie została wysłana"

@then('powinienem odebrać wiadomość "{expected_message}"')
def step_impl(context, expected_message):
    response = context.sqs.receive_message(
        QueueUrl=context.queue_url,
        MaxNumberOfMessages=1
    )
    messages = response.get('Messages', [])
    assert len(messages) == 1, "Brak wiadomości w kolejce"
    actual_message = messages[0]['Body']
    assert actual_message == expected_message, \
        f"Oczekiwano '{expected_message}', otrzymano '{actual_message}'"