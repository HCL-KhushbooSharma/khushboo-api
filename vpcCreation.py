import ibm_cloud_sdk_core
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def create_vpc(api_key, service_url, vpc_name, zone, resource_group_id):
    authenticator = IAMAuthenticator(api_key)
    vpc_service = VpcV1(
        authenticator=authenticator,
        url=service_url
    )

    # Set the parameters for the new VPC
    new_vpc = {
        "name": vpc_name,
        "resource_group": {"id": resource_group_id},
        "classic_access": False,
        "default_network_acl": True,
        "default_routing_table": True,
        "default_security_group": True,
        "flow_log_enabled": False,
        "flow_log_collectors": [],
        "route_propagation": True,
        "zones": [{"name": zone}]
    }

    # Create the VPC
    response = vpc_service.create_vpc(
        new_vpc=new_vpc
    ).get_result()

