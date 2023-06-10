# Welcome to your CDK Python project!
Event-driven architectures are an architecture style that can help you boost agility and build reliable, scalable applications. Splitting an application into loosely coupled services can help each service scale independently. A distributed, loosely coupled application depends on events to communicate application change states. Each service consumes events from other services and emits events to notify other services of state changes. 

Handling errors becomes even more important when designing distributed applications. A service may fail if it cannot handle an invalid payload, dependent resources may be unavailable, or the service may time out. There may be permission errors which can cause failures. AWS services provide many features to handle error conditions which you can use to improve the resiliency of your applications.

This repository explores three use-cases and design patterns for handling failures

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth 
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

# Design pattern using SQS DLQ.

![Inter-service Communication](./images/sqs-dlq.png)

## Create stack
$ cdk deploy SQSDLQStack

## Delete stack
$ cdk destroy SQSDLQStack

# Design pattern using Lambda DLQ.
![Inter-service Communication](./images/lambda-dlq.png)

## Create stack
$ cdk deploy LambdaDlqStack

## Delete stack
$ cdk destroy LambdaDlqStack

# Design pattern using Lambda Destination.
![Inter-service Communication](./images/lambda-dest.png)

## Create stack
$ cdk deploy LambdaDestinationDlqStack

## Delete stack
$ cdk destroy LambdaDestinationDlqStack


Enjoy!
