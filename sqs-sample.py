import boto3

def create_queue():
    sqs = boto3.resource("sqs")

    queue = sqs.create_queue(QueueName="test", Attributes={"DelaySeconds":"5"})

    print(queue.url)
    print(queue.attributes.get("DelaySeconds"))

def get_queue(name = "test"):
    sqs = boto3.resource("sqs")

    queue = sqs.get_queue_by_name(QueueName=name)

    print(queue.url)
    print(queue.attributes.get("DelaySeconds"))

def list_queues():
    sqs = boto3.resource("sqs")

    for queue in sqs.queues.all():
        print(queue.url)
        print(queue.attributes["QueueArn"].split(":")[-1])

if __name__ == "__main__":
    create_queue()
    get_queue()
    list_queues()