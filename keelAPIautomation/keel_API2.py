import requests
import json
from randome import randomdata


base_url="https://keel-api-dev.talentship.io/api"

b1=randomdata.data1
b2=randomdata.data2
b4=randomdata.data4
b5=randomdata.data5
b7=randomdata.data7
b8=randomdata.data8

with open("loads.json", "r") as json_file:   
    json_data = json.load(json_file)

svg_filename = "logo.svg"
with open(svg_filename, "rb") as svg_file:
    svg_data = svg_file.read()
orgLogo = {'logo_file': (svg_filename, svg_data, 'svg+xml')}

with open("loads.json", "r") as json_file1:   
    b6 = json.load(json_file1)
 
    
# This API use for Super Admin login. 
def post1Request():
    randomdata.generate_data()
    url=base_url+ "/login" 
    res1=requests.post(url, data=b1)
    assert res1.status_code==200, "Login Failed "
    resp= res1.json()
    token1 =resp['access_token']
    # print(".......LOGIN REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")
    global head
    head = {"Authorization": f"Bearer {token1}"}
    token2 =resp['refresh_token']
    global head1
    head1={
            "refresh_token": f"Bearer {token2}"
          }
    

def checkorgname():
    organizationName =json_data['organizationName']
    url=base_url+ f"/checkorgname?organizationName={organizationName}"
    res=requests.get(url, headers=head)
    resp=res.json()
    # print(resp['data']['result']['isAvailable'])
    assert resp['data']['result']['isAvailable']== True , "The organization name is already exists"
    # print(".......CHECK ORG NAME REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")
    
    
def domainRequest():
    domaimName =json_data['subDomain']
    url=base_url+ f"/checkdomain?domain={domaimName}"
    res=requests.get(url, headers=head)
    resp=res.json()
    # print(resp['data']['result']['isAvailable'])
    assert resp['data']['result']['isAvailable']== True , "The subdomain name is already exists"
    # print(".......CHECK DOMAIN NAME REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")
    
    
def countryId():
    url=base_url+ "/countries" 
    res=requests.get(url, headers=head)
    resp=res.json()
    assert res.status_code==200 ,"the countries dose not displayed"
    # status=resp['status']
    # assert status=='success' , "country list display failure"
    # print(".......COUNTRY LIST REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")


    
def logoRequest():
    url =base_url+ "/org/logoupload"
    res = requests.post(url,headers=head,files=orgLogo)
    resp=res.json()  #how to upload svg file  
    # print(resp)
    # assert resp['status']=='Success', "Logo upload failiure"
    # logopath=resp['data']['result']['logoPath']
    # print(logopath)
    # print(".......UPLOAD LOGO REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")
    # return logopath
    

# This API use for Adding Organization by giving unique name 
def addOrganization():
    url =base_url+ "/addorganization"
    res = requests.post(url, json=json_data, headers=head)
    assert res.status_code==200, "Creation Failed "
    resp= res.json()
    global appkey
    appkey=resp['data']['result']['organization']['appKey']
    # print(".......ADD ORGANIZATION  IS DONE.......")
    # print(".......=====================.......\n\n")   
    
# This API used for to GET the single Organization data by passing the “appkey”  
def getRequest():
    url=base_url+"/org/" +appkey
    res3=requests.get(url, headers=head)
    assert res3.status_code==200, "Get Request Failed "
    # resp=res3.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    # print(".......GET REQUEST USING APPKEY IS DONE.......")
    # print(".......=====================.......\n\n")

# This API use for List all organization present in DB and we get the total count of “records” in response 
def listdb():
    url=base_url+ "/allorganization?page=1&limit=10"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Get Request Failed "
    # resp=res4.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    # print(".......DISPLAY REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")

# This API use for List all designation present in DB and we get the total count of “records” in response 
def desRequest():
    url=base_url+"/designation"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Designation display request failed "
    # print(res.content)
    # print(".......DESIGNATION REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")

def addDes():
    url=base_url+"/designation"
    res=requests.post(url, json=b4, headers=head)
    # assert res.status_code==200, "Adding designation failed" 
    # # doubt
    # print(".......ADD DESIGNATION REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")

def listRoles():
    url=base_url+"/roles"
    res=requests.get(url, headers=head)
    assert res.status_code==200, "Roles display request failed"
    # print(".......LISTING ROLES REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")
    
    
def addRole():
    url=base_url+"/roles"
    res=requests.post(url, json=b5, headers=head)
    # assert res.status_code==200, "Adding roles failed"
    # # doubt
    # print(".......ADDING ROLES REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")    

def refreshToken():
    url=base_url+"/refreshtoken"
    res= requests.post(url, json=head1, headers=head)
    # resp=res.json()
    # print(res) #response 500
    # assert res.status_code==200 , "the access token was not created "
    # print(".......REFRESH REQUEST IS DONE.......")
    # print(".......=====================.......\n\n") 
    
def createEmail(): #what is the correct JSON file 
    url=base_url+"email-services/create-template" 
    res=requests.post(url,body=b6, headers=head)
    # print(res)
    # print(".......CREATE EMAIL REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")    
def emailTemplate():
    url=base_url+"email-services/allemailtemplate"
    res=requests.get(url, headers=head) 
    # print(res) #Error 404
    # assert res.status_code==200 , "Email template did't listed "
    # print(res)   
    # print(".......LISTING EMAIL TEMPLATE REQUEST IS DONE.......")
    # print(".......=====================.......\n\n")    

def emailTofSES():
    url=base_url+"/email-services/email-templates"
    res=requests.get(url,data="1", headers=head)
    print(res)
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
    
# post1Request()
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