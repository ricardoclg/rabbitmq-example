import pika


def publish_message(queue_name, message):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare(queue=queue_name)

        channel.basic_publish(exchange="", routing_key=queue_name, body=message)

        print(f" [x] Sent '{message}' to queue '{queue_name}'")
        connection.close()

    except Exception as e:
        print(f"Failed to send message: {e}")
        raise


def main():
    queue_name = "test_queue"
    msg = "Hello test"
    publish_message(queue_name, msg)


if __name__ == "__main__":
    main()
