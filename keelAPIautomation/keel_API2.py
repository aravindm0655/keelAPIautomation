import requests
import json
from datas import randomdata



base_url="https://keel-api-dev.talentship.io/api"
b1=randomdata.data1
b2=randomdata.data2
b6=randomdata.data6
b7=randomdata.data7
b8=randomdata.data8
file =randomdata.files
with open("loads.json", "r") as json_file:   
    json_data = json.load(json_file)
with open("load1.json", "r") as json_file1:   
    b4 = json.load(json_file1) 
with open("load2.json", "r") as json_file2:   
    b5 = json.load(json_file2)


 

def loginRequest():
    randomdata.generate_data()
    url=base_url+ "/login" 
    res1=requests.post(url, data=b1)
    assert res1.status_code==200, "Login Failed "
    resp= res1.json()
    token1 =resp['access_token']
    global head
    head = {"Authorization": f"Bearer {token1}"}
    

def checkOrgname():
    organizationName =json_data['organizationName']
    url=base_url+ f"/checkorgname?organizationName={organizationName}"
    res=requests.get(url, headers=head)
    resp=res.json()
    assert resp['data']['result']['isAvailable']== True , "The organization name is already exists"
    
    
def domainRequest():
    domaimName =json_data['subDomain']
    url=base_url+ f"/checkdomain?domain={domaimName}"
    res=requests.get(url, headers=head)
    resp=res.json()
    assert resp['data']['result']['isAvailable']== True , "The subdomain name is already exists"
    
    
def countryId():
    url=base_url+ "/countries" 
    res=requests.get(url, headers=head)
    resp=res.json()
    assert res.status_code==200 ,"country list display failure"
    # status=resp['status']
    # assert status=='success' , "country list display failure"


def logoRequest():
    url =base_url+ "/org/logoupload"
    res = requests.post(url, data=b6,files=file, headers=head)
    resp=res.json() 
    assert resp['status']=='Success', "Logo upload failiure"
    logopath=resp['data']['result']['logoPath']
    randomdata.modifyJsonfile(logopath)
    print(logopath)
    
    
def addOrganization():
    url =base_url+ "/addorganization"
    res = requests.post(url, json=json_data, headers=head)
    assert res.status_code==200, "Creation Failed "
    resp= res.json()
    global appkey
    appkey=resp['data']['result']['organization']['appKey']

     
def getAppkeyRequest():
    url=base_url+"/org/" +appkey
    res3=requests.get(url, headers=head)
    assert res3.status_code==200, "Get Request Failed "


def listdb():
    url=base_url+ "/allorganization?page=1&limit=10"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Get Request Failed "


def desRequest():
    url=base_url+"/designation"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Designation display request failed "
    # print(res.content)


def addDes():
    url=base_url+"/designation"
    res=requests.post(url, json=b4, headers=head)
    # print(res)
    assert res.status_code==201, "Adding designation failed" 
 

def listRoles():
    url=base_url+"/roles"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Roles display request failed"
    
    
def addRole():
    url=base_url+"/roles"
    res=requests.post(url, json=b5, headers=head)
    print(res) #response500
    # assert res.status_code==201, "Adding roles failed"

    
# def refreshToken():
#     url=base_url+"/refreshtoken"
#     res= requests.post(url, json=head1, headers=head)
#     # resp=res.json()
#     print(res) #response 500
#     # print(resp)
    # assert res.status_code==200 , "the access token was not created "
    
# def createEmail(): #what is the correct JSON file 
#     url=base_url+"email-services/create-template" 
#     res=requests.post(url,body=b6, headers=head)
#     # print(res)
    
# def emailTemplate():
#     url=base_url+"email-services/allemailtemplate"
#     res=requests.get(url, headers=head) 
    # print(res) #Error 404
    # assert res.status_code==200 , "Email template did't listed "
    # print(res) 

def emailTofSES():
    url=base_url+"/email-services/email-templates"
    res=requests.get(url,data="1", headers=head)
    # print(res)
    assert res.status_code==200 , "Email template did't retrived "


def emailTofID():#doubt
    url=base_url+"/email-services" 
    res=requests.get(url, headers=head)
    # print(res)
    # assert res.status_code==200 , "Email template did't retrived "

# otp verification....

def createPackage(): #unique values
    url=base_url+"/createpackage"
    res= requests.post(url, data=b7, headers=head)
    # print(res)
    # assert res.status_code==201 , "give unique values\nunable to create package"
  
    
def getPackage():
    url=base_url+"/getpackages"
    res= requests.get(url, headers=head)
    # print(res)
    assert res.status_code==200 , "unable to get file"


def getPakagebyID():
    url=base_url+"/getpackages?packageId=4"
    res= requests.get(url, headers=head)
    # print(res)
    assert res.status_code==200 , "unable to get file with ID"


def createFeatureP():# error 405
    url=base_url+"/createpackagefeature"
    res= requests.get(url,data=b8, headers=head)
    # print(res)
    # assert res.status_code==200 , "unable to create feature"  

      
def getFeaturesforP():
    url=base_url+"/getpackagefeatures"
    res= requests.get(url, headers=head)
    # print(res)
    assert res.status_code==200 , "unable to get feature"    
 
      
def getFeaturesforPbyID():
    url=base_url+"/getpackagefeatures?packageId=3"
    res= requests.get(url, headers=head)
    # print(res)
    assert res.status_code==200 , "unable to get feature with ID" 
    
# loginRequest()
# checkorgname()
# domainRequest()
# logoRequest()
# countryId()
# addOrganization()
# getRequest()
# listdb()
# desRequest()
# addDes()
# listRoles()
# addRole()
# refreshToken()
# createEmail()
# emailTemplate()
# emailTofSES()
# emailTofID()
# # createPackage()
# getPackage()
# getPakagebyID()
# createFeatureP()
# getFeaturesforP()
# getFeaturesforPbyID()