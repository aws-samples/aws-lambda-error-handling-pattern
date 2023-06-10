#!/usr/bin/env python3
import os

import aws_cdk as cdk

from dlq.lambda_sqs_dlq_stack import LambdaSQSDlqStack
from dlq.lambda_sns_dlq_stack import LambdaSnsDlqStack
from dlq.lambda_sns_dlq_destination_stack import LambdaSnsDlqDestinationStack


app = cdk.App()

# Stack to build Lambda function that is invoked synchronously with SQS as event source
# and DLQ associated to SQS queue.
LambdaSQSDlqStack(app, "SQSDLQStack")

# Stack to build Lambda function that is invoked asynchronously with SNS as event source
# and DLQ associated to Lambda function.
#
LambdaSnsDlqStack(app, "LambdaDlqStack")

# Stack to build Lambda function that is invoked asynchronously with SNS as event source
# and Destinations as well DLQ associated to Lambda function.
LambdaSnsDlqDestinationStack(app, "LambdaDestinationDlqStack")

app.synth()
