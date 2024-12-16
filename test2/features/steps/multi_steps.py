from behave import given, when, then

@given('istnieje kolejka SQS')
def step_impl(context):
    assert context.queue_url is not None, "Kolejka nie została utworzona"

@when('wysyłam wiadomości do kolejki')
def step_impl(context):
    for i in range(5):
        response = context.sqs.send_message(
            QueueUrl=context.queue_url,
            DelaySeconds=1,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': f'Message {i}'
                },
                'Index': {
                    'DataType': 'Number',
                    'StringValue': str(i)
                }
            },
            MessageBody=(
                f'This is message number {i}.'
            )
        )
        assert 'MessageId' in response, f"Wiadomość {i} nie została wysłana"
@then('powinienem odebrać maksymalnie 10 wiadomości')
def step_impl(context):
    response = context.sqs.receive_message(
        QueueUrl=context.queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5,  # Dłuższe oczekiwanie na wiadomości
        MessageAttributeNames=['All']
    )
    context.received_messages = response.get('Messages', [])
    assert len(context.received_messages) <= 10, "Odebrano więcej niż 10 wiadomości"
    assert len(context.received_messages) > 0, "Nie odebrano żadnych wiadomości"
@then('usunąć wszystkie wiadomości z kolejki')
def step_impl(context):
    for message in context.received_messages:
        context.sqs.delete_message(
            QueueUrl=context.queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print(f"Wiadomość {message['MessageId']} usunięta.")