import pulumi
import pulumi_aws as aws

# DynamoDB Table
crc_visitor_count = aws.dynamodb.Table("crc-visitor-count",
    attributes=[
        aws.dynamodb.TableAttributeArgs(
            name="visitorCount",
            type="S",
        ),
        aws.dynamodb.TableAttributeArgs(
            name="id",
            type="S",
        ),
    ],
    billing_mode="PAY_PER_REQUEST",
    hash_key="id",
    name="crc-visitor-count",
    point_in_time_recovery=aws.dynamodb.TablePointInTimeRecoveryArgs(
        enabled=False,
    ),
    range_key="visitorCount",
    ttl=aws.dynamodb.TableTtlArgs(
        attribute_name="",
    ),
    opts=pulumi.ResourceOptions(protect=True))

# Lambda
lambda_code = pulumi.FileArchive('./functions')
visitor_count_lambda = aws.lambda_.Function("visitor-count-lambda",
    code=lambda_code,
    architectures=["x86_64"],
    ephemeral_storage=aws.lambda_.FunctionEphemeralStorageArgs(
        size=512,
    ),
    handler="lambda_function.lambda_handler",
    logging_config=aws.lambda_.FunctionLoggingConfigArgs(
        log_format="Text",
        log_group="/aws/lambda/visitor-count-lambda",
    ),
    name="visitor-count-lambda",
    package_type="Zip",
    role="arn:aws:iam::993537431472:role/service-role/visitor-count-role",
    runtime=aws.lambda_.Runtime.PYTHON3D8,
    source_code_hash="HAPq9EReJVEC5gLavtc/gyd5vZtd9eiUGF932t0jBxY=",
    tracing_config=aws.lambda_.FunctionTracingConfigArgs(
        mode="PassThrough",
    ),
    opts=pulumi.ResourceOptions(protect=True))