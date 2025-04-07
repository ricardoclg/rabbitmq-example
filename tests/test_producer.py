"""
Test using unittest
"""

import unittest
from unittest.mock import MagicMock, patch

from rabbitmq_example.producer import publish_message


class TestProducer(unittest.TestCase):
    """
    Tests producer methods
    """

    @patch("pika.BlockingConnection")
    def test_publish_message_success(self, mock_blocking_connection):
        """
        Test publication success
        """
        # Mock configuration
        mock_connection = MagicMock()
        mock_channel = MagicMock()
        mock_blocking_connection.return_value = mock_connection
        mock_connection.channel.return_value = mock_channel
        # Test function
        publish_message("test_queue", "Hello, World!")
        # Assert calls
        mock_blocking_connection.assert_called_once()
        mock_connection.channel.assert_called_once()
        mock_channel.queue_declare.assert_called_once_with(queue="test_queue")
        mock_channel.basic_publish.assert_called_once_with(
            exchange="", routing_key="test_queue", body="Hello, World!"
        )
        mock_connection.close.assert_called_once()

    @patch("pika.BlockingConnection")
    def test_publish_message_connection_error(self, mock_blocking_connection):
        """
        Tests error handling
        """
        # Mock exception
        mock_blocking_connection.side_effect = Exception("Connection failed")

        with self.assertRaises(Exception) as context:
            publish_message("test_queue", "Hello, World!")

        self.assertEqual(str(context.exception), "Connection failed")


if __name__ == "__main__":
    unittest.main()
