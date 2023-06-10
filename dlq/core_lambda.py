from constructs import Construct
from aws_cdk import (
    Duration,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_lambda as _lambda,
    aws_lambda_event_sources as events,
)

lambda_timeout = Duration.seconds(15)
visibility_timeout = lambda_timeout.plus(Duration.seconds(5))
retention_period = Duration.minutes(60)

# for lambda dlq and destinations - maximum number of times to retry when the function returns an error,
# should be between 0 and 2, default 2.
lambda_retry_attempt = 2
# for sqs dlq - number of times the failed message can be dequeued from sqs before send to dead-letter queue,
# should be between 1 and 1000, default none.
sqs_max_receives = 3


def add_sns_event_source(scope: Construct, function: _lambda.Function,
                         topic: sns.Topic):
    """
    Add SNS topic as Lambda event source.

    Args:
        scope (Construct): the scope object, all child constructs are defined within this scope.
        function: Lambda function to add event source to.
        topic: SNS topic as the Lambda event source.
    """
    sns_dead_letter_queue = sqs.Queue(scope, "snsDeadLetterQueue")
    sns_source = events.SnsEventSource(
        topic,
        dead_letter_queue=sns_dead_letter_queue)
    function.add_event_source(sns_source)


def add_sqs_event_source(scope: Construct, function: _lambda.Function, queue: sqs.Queue):
    """
    Add SQS as Lambda event source.

    Args:
        scope (Construct): the scope object, all child constructs are defined within this scope.
        function: Lambda function to add event source to.
        queue: SQS queue as the Lambda event source.
    """
    sqs_source = events.SqsEventSource(queue, batch_size=1)
    alias = _lambda.Alias(scope, "alias", alias_name="CURRENT", version=function.current_version)
    alias.add_event_source(sqs_source)
