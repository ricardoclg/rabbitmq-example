# rabbitmq-sample

## Installation

```console
sudo apt install -y rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
pip install pika
```

## Usage

First start consumer.py at a terminal.
```bash
python3 -m consumer.py
```

Then start producer.py at another terminal.
```bash
python3 -m producer.py
```

The consumer must show the message sent by the producer

## License

`rabbitmq-sample` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
