import pytest
from create_vsi import create_vsi
 
API_KEY = '<your-IBM-Cloud-API-key>'
SERVICE_URL = '<your-IBM-Cloud-service-url>'
INSTANCE_NAME = 'test-instance'
INSTANCE_IMAGE_ID = '<your-IBM-Cloud-image-id>'
INSTANCE_PROFILE_NAME = 'cx2-2x4'
ZONE_NAME = 'us-south-1'
SUBNET_NAME = 'test-subnet'
SG_NAME = 'test-security-group'
VPC_NAME = 'test-vpc'
VOLUME_PROFILE_NAME = 'general-purpose'
PLACEMENT_GROUP_NAME = 'test-placement-group'
 
@pytest.fixture
def vsi():
    instance = create_vsi(
        api_key=API_KEY,
        service_url=SERVICE_URL,
        instance_name=INSTANCE_NAME,
        instance_image_id=INSTANCE_IMAGE_ID,
        instance_profile_name=INSTANCE_PROFILE_NAME,
        zone_name=ZONE_NAME,
        subnet_name=SUBNET_NAME,
        sg_name=SG_NAME,
        ssh_keys=[],
        vpc_name=VPC_NAME,
        volume_profile_name=VOLUME_PROFILE_NAME,
        placement_group_name=PLACEMENT_GROUP_NAME,
    )
    yield instance
    # cleanup the created instance
 
def test_create_vsi(vsi):
    assert vsi['id'] is not None
    assert vsi['name'] == INSTANCE_NAME
    assert vsi['status']['name'] == 'running'
