import json
import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def handler(event: dict, context):
    """
    The handler to send message to DLQ or on-failure destination.

    Args:
        event (dict): contains the data received from its data source.
        context: contains the lambda invocation context.
    """
    logger.info(f"event - {event}")
    for record in event['Records']:
        if 'Sns' in record:
            payload = json.loads(record["Sns"]['Message'])
        else:
            payload = json.loads(record["body"])
        if not payload["pass"]:
            raise ValueError("Fail the Lambda function.")
