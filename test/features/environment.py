from moto import mock_aws
import boto3

def before_all(context):
    # Uruchomienie mocka jako kontekstu
    context.mock = mock_aws()
    context.mock.start()

    # Utworzenie klienta AWS SQS
    context.sqs = boto3.client('sqs', region_name='us-east-1')

    # Utworzenie testowej kolejki
    response = context.sqs.create_queue(
        QueueName="TestQueue",
        Attributes={"VisibilityTimeout": "60"}
    )

    # Sprawdzanie odpowiedzi
    context.queue_url = response.get("QueueUrl")
    if not context.queue_url:
        raise RuntimeError("Nie udało się utworzyć kolejki SQS.")
    print(f"Kolejka SQS utworzona: {context.queue_url}")

def after_all(context):
    context.mock.stop()