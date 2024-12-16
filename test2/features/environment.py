from moto import mock_aws
import boto3

def before_all(context):
    # Uruchomienie mocka
    context.mock = mock_aws()
    context.mock.start()

    # Utworzenie klienta AWS SQS
    context.sqs = boto3.client('sqs', region_name='us-east-1')

    # Utworzenie testowej kolejki
    response = context.sqs.create_queue(
        QueueName="TestQueue",
        Attributes={"VisibilityTimeout": "60"}
    )

    # Przypisanie URL kolejki
    context.queue_url = response['QueueUrl']
    print(f"Kolejka SQS utworzona: {context.queue_url}")

def after_all(context):
    context.mock.stop()