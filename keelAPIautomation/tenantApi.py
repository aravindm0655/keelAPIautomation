import requests
import json
from tenetdatas import RandomData


d1=RandomData.data1
d7=RandomData.data7
d8=RandomData.data8
d12=RandomData.data12
d13=RandomData.data13
d14=RandomData.data14
d15=RandomData.data15
d16=RandomData.data16
eid=129
id=5 #id change 
base_url="https://keel-tenants-dev.talentship.io"

with open("loads.json", "r") as json_file:   
    json_data = json.load(json_file)


def loginRequest():
    RandomData.generate_data()
    url=base_url+ "/auth/login" 
    res=requests.post(url, data=d1)
    print(res)#response 200
    assert res.status_code==200, "Login Failed "
    resp= res.json()
    token1 =resp['access_token']
    # print(token1)
    global head
    head = {"Authorization": f"Bearer {token1}"}
    

    
def orgList():
    url=base_url+"/api/v1/organizations"
    res= requests.get(url , headers=head)
    print(res)#response 200
    assert res.status_code==200, "Listing Organiztion failed "
    resp=res.json()
    result_array = resp["data"]["result"]
    global appkey
    for org in result_array:
        if org["id"] == 66:
            appkey = org["appKey"]
            break

def addBasics():
    url=base_url+f"/tenantapi/v1/{appkey}/employee/addbasic"
    with open("data2.json", "r") as json_file:   
        d2 = json.load(json_file)
    res= requests.post(url, data=d2, headers=head)
    print(res)#response 200
    assert res.status_code==200, "Adding basic infos Failed"
    
def designation():
    url=base_url+f"/tenantapi/v1/{appkey}/designation"
    with open("data3.json", "r") as json_file:   
        d3 = json.load(json_file)
    res=requests.post(url, json=d3, headers=head)
    print(res)# response 201
    assert res.status_code==201, "Adding designation Failed "
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))
    
def designationlist():
    url=base_url+f"/tenantapi/v1/{appkey}/designation"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "Listing Designation Failed"
    
def employeebyAppkey():
    url=base_url+f"/tenantapi/v1/{appkey}/allemployees"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200,"Diaplaying employee by app key failed "
    
def orgbyAppkey():
    url=base_url+f"/tenantapi/v1/{appkey}/organization"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "Diaplaying Organization by app key failed"

def employeeby_uuid():
    uuid="23f52efa-70d2-4a14-b9b1-5c591d1acf0c"
    url=base_url+f"/tenantapi/v1/{appkey}/retrieve/{uuid}"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "Diaplaying employee by uuid failed"

def perdonalIndobyEid():
    url=base_url+f"/tenantapi/v1/{appkey}/listpersonalinformation/{eid}"
    res=requests.get(url, headers=head)
    print(res)
    assert res.status_code==200, "Diaplaying personal info  by employee id  failed"


def updateInfobyEid():
    url=base_url+f"/tenantapi/v1/{appkey}/personalinformation/{eid}"
    with open("data4.json", "r") as json_file:   
        d4 = json.load(json_file)
    res=requests.put(url, data=d4, headers=head)
    print(res)
    # assert res.status_code==200, "Diaplaying Organization by app key failed"
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))
    
def createEdu():
    url=base_url+f"/api/v1/educationtypes"
    with open("data5.json", "r") as json_file:   
        d5 = json.load(json_file)
    res=requests.post(url,json=d5, headers=head)
    print(res)
    assert res.status_code==201, "Creating education type failed"


def listEdu():
    url=base_url+"/api/v1/educationtypes"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "listing education type is failed"
    
def addGender():
    url=base_url+"/api/v1/gendertypes"
    with open("data6.json", "r") as json_file:   
        d6 = json.load(json_file)    
    res=requests.post(url,json=d6, headers=head)
    print(res) #response 201
    assert res.status_code==201, "Adding new gender failed"
    
def listGender():
    url=base_url+"/api/v1/gendertypes"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "Lisiting gender failed"
    
def uploadProfile():
    url=base_url+f"/tenantapi/v1/{appkey}/profileupload"
    with open("C:/Users/aravi/Desktop/keelAPIautomation/RZFZ7102.JPG", "rb") as image_file:
        file = {"image": image_file}
        res=requests.post(url,data=d7,files=file, headers=head) #missing required params
    print(res)
    resp=res.json()
    print(json.dumps(resp ,indent=4))
    # assert res.status_code==200, "Upload profile pic failed"
    
def uploadDoc():
    print("   ") #params

    
def listEDU():
    url=base_url+f"/tenantapi/v1/{appkey}/listeducationinformation/{eid}"
    res=requests.get(url, headers=head)
    print(res)
    assert res.status_code==200, "Lisiting education of the user failed"
    
# delete employee education

def updateFamDatails():
    url=base_url+f"/tenantapi/v1/{appkey}/familydetails/{eid}"
    res=requests.put(url,data=d8, headers=head)
    print(res) #error 404

def getFamDatails():
    url=base_url+f"/tenantapi/v1/{appkey}/listfamilydetails/{eid}"
    res=requests.get(url, headers=head)
    print(res) #error 404

def getRelationType():
    url=base_url+"/api/v1/relationshiptypes"
    res=requests.get(url, headers=head)
    print(res) #response 200
    assert res.status_code==200, "listing reletionship type failed"
  
def getSkill():
    url=base_url+f"/tenantapi/v1/{appkey}/skill?searchSkill=angular"
    res=requests.get(url, headers=head)
    print(res) #response 200  
    assert res.status_code==200, "Lisiting skills failed"

def addSkill():
    url=base_url+f"/tenantapi/v1/{appkey}/skill"
    b9={
    "skill": "Ionic1"
    }
    res=requests.post(url,data=b9, headers=head)
    print(res) #response 500  
    # assert res.status_code==200, "Lisi=ting gender failed"

def previousEmployment(): # not executed 
    url=base_url+f"/tenantapi/v1/{appkey}/addpreviousemployment"
    with open("data10.json", "r") as json_file:   
        d10 = json.load(json_file)       
    res=requests.post(url, data=d10, headers=head)
    print(res)
    
def updatePreEmp():  # not executed
    url=base_url+f"/tenantapi/v1/{appkey}/previousemployment/{eid}/{id}"
    with open("data11.json", "r") as json_file:   
        d11 = json.load(json_file)   
    res=requests.post(url, data=d11, headers=head)
    print(res)

def listPreEmp():
    url=base_url+f"/tenantapi/v1/{appkey}/listpreviousemployment/{eid}?id={id}"
    res= requests.get(url, headers=head)
    print(res)

def deletePreEmp():
    url=base_url+f"/tenantapi/v1/{appkey}/previousemployment/{eid}/{id}"
    res= requests.delete(url, headers=head)
    print(res)

def uploadPreEmpDoc():
    url=base_url+f"/tenantapi/v1/{appkey}/previousemploymentdocumentupload"
    with open("C:/Users/aravi/Desktop/keelAPIautomation/RZFZ7102.JPG", "rb") as image_file:
        file = {"image": image_file}
    res=requests.post(url, bata=d1 ,files=file, headers=head)


def proofType():
    url=base_url+"/api/v1/prooftypes"
    d11={
        "proofType":["pan card"]
    }
    res=requests.post(url, data=d11, headers=head)

def listProofType():
    url=base_url+f"/api/v1/prooftypes"
    res=requests.get(url,headers=head) 
    print(res)
    assert res.status_code==200, "Lisiting proof types failed"
    
def uploadEmpId(): #doubts
    url=base_url+f"/tenantapi/v1/{appkey}/identificationupload"
    with open("C:/Users/aravi/Desktop/keelAPIautomation/RZFZ7102.JPG", "rb") as image_file:
        file = {"image": image_file}
    res=requests.post(url,data=d12, files=file, headers=head)
    print(res)
    
def addEmpId():
    url=base_url+f"/tenantapi/v1/{appkey}/employee-identification"
    res=requests.post(url, data=d13, headers=head)
    print(res)
    
def listEmpId():
    url=base_url+f"/tenantapi/v1/{appkey}/Listidentification/{eid}" 
    res=requests.get(url, headers=head)
    print(res)
    assert res.status_code==200, "Lisiting Employment identification Documents  failed"

def deleteEmpid():
    url= base_url+f"/tenantapi/v1/{appkey}/identificationdetails/{eid}"
    res=requests.delete(url, headers=head)
    print(res)

def addCalc():
    url=base_url+f"/tenantapi/v1/{appkey}/calculator"
    res=requests.post(url,data=d14,headers=head) #modify data
    print(res)

def uploadEmpStstus():
    url=base_url+f"/tenantapi/v1/{appkey}/updateEmployeeStatus"
    res=requests.put(url, data=d15,headers=head) #checjk data
    print(res)

def updateEmpPortal():
    url=base_url+f"/tenantapi/v1/{appkey}/employee/updatebasic/{eid}"
    res=requests.put(url, data=d16,headers=head)
    print(res)


# loginRequest()
# orgList()
# addBasics()
# designation()
# designationlist()
# employeebyAppkey()
# orgbyAppkey()
# employeeby_uuid()
# perdonalIndobyEid()
# updateInfobyEid()
# createEdu()
# listEdu()
# # addGender()
# listGender()
# uploadProfile()
# listEDU()
# updateFamDatails()
# getFamDatails()
# getRelationType()
# getSkill()
# addSkill()
# previousEmployment()
# updatePreEmp()
# listPreEmp()
# deletePreEmp()
# uploadPreEmpDoc()
# proofType()
# listProofType()
# uploadEmpId()
# addEmpId()
# listEmpId()
# deleteEmpid()
# addCalc()
# uploadEmpStstus()
# updateEmpPortal()