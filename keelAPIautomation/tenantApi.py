import requests
import json
from tenetdatas import RandomData

base_url="https://keel-tenants-dev.talentship.io"
d1=RandomData.data1
d8=RandomData.data8
d12=RandomData.data12
d13=RandomData.data13
d14=RandomData.data14
d15=RandomData.data15
d16=RandomData.data16
d17=RandomData.data17
d18=RandomData.data18
dx=RandomData.datax
file1 =RandomData.file1
file2=RandomData.file2
file3=RandomData.file3
file4=RandomData.file4
eid=129
uuid="23f52efa-70d2-4a14-b9b1-5c591d1acf0c"
# with open("loads.json", "r") as json_file:   
#     json_data = json.load(json_file)


def loginRequest(): 
    RandomData.generate_data()
    # RandomData.modify()
    url=base_url+ "/auth/login" 
    res=requests.post(url, data=d1)
    # print(res)
    assert res.status_code==200, "Login Failed "
    resp= res.json()
    token1 =resp['access_token']
    # print(json.dumps(resp, indent=4))
    global head
    head = {"Authorization": f"Bearer {token1}"}
     
def orgList():
    url=base_url+"/api/v1/organizations"
    res= requests.get(url , headers=head)
    # print(res)#response 200
    assert res.status_code==200, "Listing Organiztion failed "
    resp=res.json()
    # print(json.dumps(resp, indent=4))
    result_array = resp["data"]["result"]
    global appkey
    for org in result_array:
        if org["id"] == 66:
            appkey = org["appKey"]
            # print(appkey)
            break

def addBasics():
    url=base_url+f"/tenantapi/v1/{appkey}/employee/addbasic"
    with open("data2.json", "r") as json_file:   
        d2 = json.load(json_file)
    res= requests.post(url, data=d2, headers=head)
    # print(res)
    resp= res.json()
    print(json.dumps(resp, indent=4))
    assert resp["message"]=="Data saved successfully", "Adding basic infos Failed"
    
def designation():
    url=base_url+f"/tenantapi/v1/{appkey}/designation"
    with open("data3.json", "r") as json_file:   
        global d3
        d3 = json.load(json_file)
    res=requests.post(url, json=d3, headers=head)
    # print(res)# response 201
    resp=res.json()
    # print(json.dumps(resp ,indent=4))
    dID=resp["data"]["result"][0]["id"]
    des=d3["designation"]
    assert resp["data"]["result"][0]["designation"]==des[0], "Adding designation Failed "
    return dID
    
def designationlist(dID):
    url=base_url+f"/tenantapi/v1/{appkey}/designation"
    res=requests.get(url, headers=head)
    # print(res) #response 200
    resp=res.json()
    # print(json.dumps(resp ,indent=4))
    for item in resp['data']['result']:
        if item['id'] == dID:
            designation = item['designation']
            break
    des=d3["designation"]
    assert designation==des[0], "Listing Designation API Failed"
    
def employeebyAppkey(): # assertion 
    url=base_url+f"/tenantapi/v1/{appkey}/allemployees"
    res=requests.get(url, headers=head)
    print(res) #response 200
    resp=res.json()
    print(json.dumps(resp ,indent=4)) 
    assert res.status_code==200,"Diaplaying employee by app key failed "
    
def orgbyAppkey(): # assertion 
    url=base_url+f"/tenantapi/v1/{appkey}/organization"
    res=requests.get(url, headers=head)
    print(res) #response 200
    resp=res.json()
    print(json.dumps(resp ,indent=4))
    assert res.status_code==200, "Diaplaying Organization by app key failed"

def employeeby_uuid(): # assertion 
    url=base_url+f"/tenantapi/v1/{appkey}/retrieve/{uuid}"
    res=requests.get(url, headers=head)
    print(res) #response 200
    resp=res.json()
    print(json.dumps(resp ,indent=4))
    assert res.status_code==200, "Diaplaying employee by uuid failed"

def perdonalIndobyEid(): # assertion 
    url=base_url+f"/tenantapi/v1/{appkey}/listpersonalinformation/{eid}"
    res=requests.get(url, headers=head)
    print(res)
    resp=res.json()
    print(json.dumps(resp ,indent=4))
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

def listGender():
    url=base_url+"/api/v1/gendertypes"
    res=requests.get(url, headers=head)
    print(res) #response 200
    # resp=res.json() 
    # print(json.dumps(resp ,indent=4))   
    assert res.status_code==200, "Lisiting gender failed"
        
def addGender():
    url=base_url+"/api/v1/gendertypes"
    with open("data6.json", "r") as json_file:   
        d6 = json.load(json_file)    
    res=requests.post(url,json=d6, headers=head)
    print(res) #response 201
    assert res.status_code==201, "Adding new gender failed"
    
def getRelationType():
    url=base_url+"/api/v1/relationshiptypes"
    res=requests.get(url, headers=head)
    print(res) #response 200
    resp=res.json() 
    print(json.dumps(resp ,indent=4))   
    assert res.status_code==200, "listing reletionship type failed"
    
def uploadProfile():
    url=base_url+f"/tenantapi/v1/{appkey}/profileupload"
    res=requests.post(url, data=d12,files=file1, headers=head) 
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))
    # assert res.status_code==200, "Upload profile pic failed"
    
def uploadDoc():
    url=base_url+f"/tenantapi/v1/{appkey}/educationdocumentupload"
    res=requests.post(url, data=d12,files=file4, headers=head) 
    print(res)
    assert res.status_code==201, "Upload doc failed"
 
def listEDUinfo():
    url=base_url+f"/tenantapi/v1/{appkey}/listeducationinformation/{eid}"
    res=requests.get(url, headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200, "Lisiting education of the user failed"
    
def createFamDetails():
    url=base_url+f"/tenantapi/v1/{appkey}/employee-family-details"
    res=requests.post(url, json=dx, headers= head)
    print(res)
    resp=res.json()
    print(json.dumps(resp, indent=4))

def updateFamDatails():
    url=base_url+f"/tenantapi/v1/{appkey}/familydetails/106"
    res=requests.put(url,data=d8, headers=head)
    print(res) 
    assert res.status_code==200, "update family detail failed failed"
    # resp=res.json()
    # print(json.dumps(resp, indent=4))    
    
def getFamDatails():
    url=base_url+f"/tenantapi/v1/7862-6A71-CE38-3D27/listFamily/129"
    res=requests.get(url, headers=head)
    print(res) 
    assert res.status_code==200, "Lisiting family failed"
    # resp=res.json()
    # print(json.dumps(resp, indent=4))

def getSkill():
    url=base_url+f"/tenantapi/v1/{appkey}/skill?searchSkill=angular"
    res=requests.get(url, headers=head)
    print(res) #response 200  
    assert res.status_code==200, "Lisiting skills failed"
    # resp=res.json()
    # print(json.dumps(resp, indent=4))

def addSkill():
    url=base_url+f"/tenantapi/v1/{appkey}/skill"
    b9={
    "skill": "skills"
    }
    res=requests.post(url,data=b9, headers=head)
    print(res) #response 500  
    # assert res.status_code==200, "adding skills failed"

def addPreEmp():
    url=base_url+f"/tenantapi/v1/{appkey}/addpreviousemployment"
    with open("data13.json", "r") as json_file:   
        d13 = json.load(json_file)     
    res=requests.post(url,json=d13,headers=head)
    print(res)
    resp=res.json()
    global id
    id=resp['data']['result']['id']
    # print(id)
    # print(json.dumps(resp ,indent=4))
       
def listPreEmp():
    url=base_url+f"/tenantapi/v1/{appkey}/listpreviousemployment/{eid}?id={id}"
    res= requests.get(url, headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))  
    
def updatePreEmp():  
    url=base_url+f"/tenantapi/v1/{appkey}/previousemployment/{eid}/{id}"
    with open("data10.json", "r") as json_file:   
        d10 = json.load(json_file)   
    res=requests.put(url, json=d10, headers=head)
    print(res)
    resp=res.json()
    print(json.dumps(resp ,indent=4))

def deletePreEmp():
    url=base_url+f"/tenantapi/v1/{appkey}/previousemployment/{eid}/{id}"
    res= requests.delete(url, headers=head)
    print(res)

def uploadPreEmpDoc():
    url=base_url+f"/tenantapi/v1/{appkey}/previousemploymentdocumentupload"
    res=requests.post(url, data=d17,files=file2, headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))

def listProofType():
    url=base_url+f"/api/v1/prooftypes"
    res=requests.get(url,headers=head) 
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))    
    assert res.status_code==200, "Lisiting proof types failed"
    
def proofType():   
    url=base_url+"/api/v1/prooftypes"
    with open("data11.json", "r") as json_file:   
        d11 = json.load(json_file)  
    res=requests.post(url, json=d11, headers=head)
    print(res)
    
def uploadEmpId():  
    url=base_url+f"/tenantapi/v1/{appkey}/identificationupload"
    res=requests.post(url, data=d18, files=file3, headers=head)
    print(res) 
    # resp=res.json()
    # print(json.dumps(resp, indent=4))
    
def addEmpId():
    url=base_url+f"/tenantapi/v1/{appkey}/employee-identification"
    res=requests.post(url, json=d13, headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))  
    
def listEmpId():
    url=base_url+f"/tenantapi/v1/{appkey}/Listidentification/{eid}" 
    res=requests.get(url, headers=head)
    print(res)
    resp=res.json()
    # print(json.dumps(resp ,indent=4)) 
    global pk
    pk=resp['data']['result']['Identification'][0]['Id']
    assert res.status_code==200, "Lisiting Employment identification Documents  failed"

def deleteEmpid():
    url= base_url+f"/tenantapi/v1/{appkey}/identificationdetails/{eid}/{pk}" 
    res=requests.delete(url, headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))  

def addCalc():
    url=base_url+f"/tenantapi/v1/{appkey}/calculator"
    res=requests.post(url,data=d14,headers=head) 
    print(res)

def uploadEmpStstus():
    url=base_url+f"/tenantapi/v1/{appkey}/updateEmployeeStatus"
    res=requests.put(url, data=d15,headers=head) #checjk data
    print(res)

def updateEmpPortal():
    url=base_url+f"/tenantapi/v1/{appkey}/employee/updatebasic/{eid}"
    res=requests.put(url, json=d16,headers=head)
    print(res)
    # resp=res.json()
    # print(json.dumps(resp ,indent=4))

def employeeprofiledetails():
    url = base_url+f"/tenantapi/v1/{appkey}/myprofile/{uuid}"
    res=requests.get(url, headers=head)
    resp=res.json()
    print(json.dumps(resp, indent=4))

loginRequest() #.......................200
orgList()#.............................200
# addBasics() #..........................200 
# dID=designation() #....................201
# designationlist(dID)    #..............200
# employeebyAppkey()   #.................200
# orgbyAppkey()  #.......................200
# employeeby_uuid()  #...................200
# perdonalIndobyEid() #..................200
# updateInfobyEid()   #..................200
# createEdu() #..........................201
# listEdu()  #...........................200
# addGender()  #.........................201  
# listGender() #.........................200
# getRelationType() #....................200  
# uploadProfile() #......................201 
# uploadDoc() #..........................201
# listEDUinfo() #........................200   
# # createFamDetails() #...................200 :400
# updateFamDatails()    #................200
# getFamDatails()   #....................200 
# getSkill() #...........................200
# addSkill() #...........................200     
# addPreEmp() #..........................200
# listPreEmp()  #........................200  
# updatePreEmp()   #.....................200    
# deletePreEmp()  #......................200 
# uploadPreEmpDoc()#.....................200  
# listProofType()  #.....................200  
# proofType()  #.........................201  
# uploadEmpId() #........................201  
# addEmpId()  #..........................200  
# listEmpId()  #.........................200
# deleteEmpid()  #.......................200  
# addCalc()  #...........................200  
# uploadEmpStstus() #....................200
# updateEmpPortal() #....................200 
employeeprofiledetails()