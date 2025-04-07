"""
Consumer module for RabbitMQ
"""

import pika


def start_consumer(queue_name: str, callback):
    """
    Start consumer and specify RabbitMQ queue

    Args:
        queue_name (str): Name of the queue to start
        callback (Any): The consumer callbacks are dispatched only in the scope of
        specially-designated methods

    Raises:
        Exception: If RabbitMQ fails to start consumer
    """
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
    def callback_example(body):
        """
        Some callback example
        """
        print(f" [x] Mensagem recebida: {body.decode()}")

    queue_name = "test_queue"
    start_consumer(queue_name, callback_example)


if __name__ == "__main__":
    main()
