"""
Test using unittest
"""

import unittest
from unittest.mock import MagicMock, patch

from rabbitmq_example.consumer import start_consumer


class TestConsumer(unittest.TestCase):
    """
    Test for consumer methods
    """

    @patch("pika.BlockingConnection")
    def test_start_consumer_success(self, mock_blocking_connection):
        """
        Tests consumer start success
        """
        # Mock configuration
        mock_connection = MagicMock()
        mock_channel = MagicMock()
        mock_blocking_connection.return_value = mock_connection
        mock_connection.channel.return_value = mock_channel
        test_callback = MagicMock()
        # Test function
        start_consumer("test_queue", test_callback)
        # Assert calls
        mock_blocking_connection.assert_called_once()
        mock_connection.channel.assert_called_once()
        mock_channel.queue_declare.assert_called_once_with(queue="test_queue")
        mock_channel.basic_consume.assert_called_once_with(
            queue="test_queue", auto_ack=True, on_message_callback=test_callback
        )
        mock_channel.start_consuming.assert_called_once()

    @patch("pika.BlockingConnection")
    def test_start_consumer_connection_error(self, mock_blocking_connection):
        """
        Tests error handling
        """
        # Mock connection exception
        mock_blocking_connection.side_effect = Exception("Connection failed")
        test_callback = MagicMock()

        with self.assertRaises(Exception) as context:
            start_consumer("test_queue", test_callback)

        self.assertEqual(str(context.exception), "Connection failed")


if __name__ == "__main__":
    unittest.main()
