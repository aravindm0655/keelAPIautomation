import pytest

from tenantApi import (
    loginRequest,
    orgList,
    addBasics,
    designation,
    designationlist,
    employeebyAppkey,
    orgbyAppkey,
    employeeby_uuid,
    perdonalIndobyEid,
    updateInfobyEid,
    createEdu,
    listEdu,
    # addGender()
    listGender,
    uploadProfile,
    listEDU,
    updateFamDatails,
    getFamDatails,
    getRelationType,
    getSkill,
    addSkill
)

@pytest.fixture(scope="module")
def setup_api_environment():
    yield


def test_1(setup_api_environment):
    loginRequest()

def test_2(setup_api_environment):
    orgList()

def test_3(setup_api_environment):
    addBasics()

def test_4(setup_api_environment):
    designation()
     
def test_5(setup_api_environment):
    designationlist()

def test_6(setup_api_environment):
    employeebyAppkey()
    
def test_7(setup_api_environment):
    orgbyAppkey()
    
def test_8(setup_api_environment):
    employeeby_uuid()
    
def test_9(setup_api_environment):
    perdonalIndobyEid()
    
def test_10(setup_api_environment):
    updateInfobyEid()
    
def test_11(setup_api_environment):
    createEdu()
    
def test_12(setup_api_environment):
    listEdu()    

# def test_13(setup_api_environment):
#     addGender()
    
def test_14(setup_api_environment):
    listGender()
    
def test_15(setup_api_environment):
    uploadProfile()
    
def test_16(setup_api_environment):
    listEDU()
    
def test_17(setup_api_environment):
    updateFamDatails()
    
def test_18(setup_api_environment):
    getFamDatails()
    
def test_19(setup_api_environment):
    getRelationType()
    
def test_20(setup_api_environment):
    getSkill()
    
def test_21(setup_api_environment):
    addSkill()
    
def test_22(setup_api_environment):
    getFeaturesforP()
    
def test_23(setup_api_environment):
    getFeaturesforPbyID()
    
    
if __name__ == "__main__":
    pytest.main()

