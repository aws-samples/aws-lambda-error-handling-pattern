from aws_cdk import (
    aws_sns as sns,
    aws_lambda as _lambda,
    Stack,
)
from constructs import Construct
from dlq import core_lambda


class LambdaSnsDlqStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """
        Constructor for Lambda function with SNS as event source and Lambda DLQ for un-successfully processed events.

        Args:
            scope (Construct): the scope object, all child constructs are defined within this scope.
            construct_id(str): id for the construct, used uniquely.
        """
        super().__init__(scope, construct_id, **kwargs)

        # create SNS topic for aggregate data notification.
        topic = sns.Topic(
            self, "topic",
            display_name="topic",
            topic_name="lambda_topic")

        # create lambda function.
        function = _lambda.Function(
            self, "lambda",
            function_name="dlq_lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda.handler",
            code=_lambda.Code.from_asset(path="dlq/function"),
            dead_letter_queue_enabled=True,
            retry_attempts=core_lambda.lambda_retry_attempt,
            timeout=core_lambda.lambda_timeout, **kwargs)

        # associate lambda with sns as event source.
        core_lambda.add_sns_event_source(self, function, topic)

