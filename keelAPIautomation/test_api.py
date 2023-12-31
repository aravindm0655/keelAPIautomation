import pytest

from keel_API2 import (
    loginRequest,
    checkOrgname,
    domainRequest,
    logoRequest,
    countryId,
    addOrganization,
    getAppkeyRequest,
    listdb,
    desRequest,
    addDes, 
    listRoles,
    addRole, 
    # refreshToken,
    # createEmail,
    # emailTemplate,
    emailTofSES,
    emailTofID,
    createPackage,
    getPackage,
    getPakagebyID,
    createFeatureP,
    getFeaturesforP,
    getFeaturesforPbyID
)

@pytest.fixture(scope="module")
def setup_api_environment():
    yield


def test_1(setup_api_environment):
    loginRequest()

def test_2(setup_api_environment):
    checkOrgname()

def test_3(setup_api_environment):
    domainRequest()

def test_4(setup_api_environment):
    logoRequest()
     
def test_5(setup_api_environment):
    countryId()

def test_6(setup_api_environment):
    addOrganization()
    
def test_7(setup_api_environment):
    getAppkeyRequest()
    
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

# def test_13(setup_api_environment):
#     refreshToken()
    
# def test_14(setup_api_environment):
#     createEmail()
    
# def test_15(setup_api_environment):
#     emailTemplate()
    
def test_16(setup_api_environment):
    emailTofSES()
    
def test_17(setup_api_environment):
    emailTofID()
    
def test_18(setup_api_environment):
    createPackage()
    
def test_19(setup_api_environment):
    getPackage()
    
def test_20(setup_api_environment):
    getPakagebyID()
    
def test_21(setup_api_environment):
    createFeatureP()
    
def test_22(setup_api_environment):
    getFeaturesforP()
    
def test_23(setup_api_environment):
    getFeaturesforPbyID()
    
    
if __name__ == "__main__":
    pytest.main()

