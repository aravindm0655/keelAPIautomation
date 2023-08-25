import pytest

from keel_API2 import (
    post1Request,
    checkorgname,
    domainRequest,
    logoRequest,
    countryId,
    addOrganization,
    getRequest,
    listdb,
    desRequest,
    addDes,
    listRoles,
    addRole,
    # refreshToken,
    # createEmail,
    # emailTemplate
)

@pytest.fixture(scope="module")
def setup_api_environment():
    yield


def test_1(setup_api_environment):
    post1Request()

def test_2(setup_api_environment):
    checkorgname()

def test_3(setup_api_environment):
    domainRequest()

def test_4(setup_api_environment):
    logoRequest()
     
def test_5(setup_api_environment):
    countryId()

def test_6(setup_api_environment):
    addOrganization()
    
def test_7(setup_api_environment):
    getRequest()
    
def test_8(setup_api_environment):
    listdb()
    
def test_9(setup_api_environment):
    desRequest()
    
def test_10(setup_api_environment):
    addDes()
    
def test_11(setup_api_environment):
    listRoles()
    
def test_12(setup_api_environment):
    addRole()    
    
    
# Run pytest when this script is executed
if __name__ == "__main__":
    pytest.main()
