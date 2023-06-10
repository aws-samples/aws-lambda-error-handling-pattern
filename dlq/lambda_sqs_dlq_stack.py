from aws_cdk import (
    aws_sqs as sqs,
    aws_lambda as _lambda,
    Stack,
)
from constructs import Construct

from dlq import core_lambda


class LambdaSQSDlqStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create dlq for sqs queue.
        dlq = sqs.Queue(
            self, "sqs-dlq",
            retention_period=core_lambda.retention_period,
            visibility_timeout=core_lambda.visibility_timeout)
        # create sqs queue.
        queue = sqs.Queue(
            self, "sqs",
            retention_period=core_lambda.retention_period,
            visibility_timeout=core_lambda.visibility_timeout,
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=core_lambda.sqs_max_receives,
                queue=dlq))

        # create lambda function.
        function = _lambda.Function(
            self, "lambda",
            function_name="dlq_lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda.handler",
            code=_lambda.Code.from_asset(path="dlq/function"),
            timeout=core_lambda.lambda_timeout, **kwargs)

        # associate lambda with sqs as event source.
        core_lambda.add_sqs_event_source(self, function, queue)
