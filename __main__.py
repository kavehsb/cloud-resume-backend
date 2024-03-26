import pulumi
import pulumi_aws as aws

# DynamoDB Table (crc-visitor-count-table)
crc_visitor_count_table = aws.dynamodb.Table("crc-visitor-count-table",
    attributes=[aws.dynamodb.TableAttributeArgs(
        name="id",
        type="S",
    )],
    billing_mode="PAY_PER_REQUEST",
    hash_key="id",
    name="crc-visitor-count-table",
    point_in_time_recovery=aws.dynamodb.TablePointInTimeRecoveryArgs(
        enabled=False,
    ),
    ttl=aws.dynamodb.TableTtlArgs(
        attribute_name="",
    ),
    opts=pulumi.ResourceOptions(protect=True))

# Lambda function (visitor-count-lambda)
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
    tracing_config=aws.lambda_.FunctionTracingConfigArgs(
        mode="PassThrough",
    ),
    opts=pulumi.ResourceOptions(protect=True))

# API Gateway (crc-api-gateway)
crc_api_gateway = aws.apigateway.RestApi("crc-api-gateway",
    api_key_source="HEADER",
    endpoint_configuration=aws.apigateway.RestApiEndpointConfigurationArgs(
        types="REGIONAL",
    ),
    name="crc-api-gateway",
    opts=pulumi.ResourceOptions(protect=True))