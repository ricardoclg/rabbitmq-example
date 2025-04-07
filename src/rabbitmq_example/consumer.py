import pika


def start_consumer(queue_name, callback):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare(queue=queue_name)

        channel.basic_consume(
            queue=queue_name, auto_ack=True, on_message_callback=callback
        )

        print(f" [*] Waiting for messages in {queue_name}. To exit press CTRL+C")
        channel.start_consuming()

    except Exception as e:
        print(f"Failed to start consumer: {e}")
        raise


def main():
    def callback_example(ch, method, properties, body):
        print(f" [x] Mensagem recebida: {body.decode()}")

    queue_name = "test_queue"
    start_consumer(queue_name, callback_example)


if __name__ == "__main__":
    main()
