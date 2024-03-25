import pulumi
import pulumi_aws as aws

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