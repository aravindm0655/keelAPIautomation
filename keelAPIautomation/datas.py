import random
import string
import json

class randomdata:
    
    data1= {
        "user_name" : "admin",
        "password": "Admin@123"
    }
    
    data2={
        "firstName": "super1",
        "lastName": "admin1",
        "userName":"admin1",
        "email":"admin1@123",
        "password": "Admin1@123"
    }
    
    
    files = {
        "orgLogo": ("logo.svg", open("C:/Users/aravi/Desktop/keelAPIautomation/logo.svg", "rb"), "image/svg+xml")
    }
    data6 = {
    "orgLogo": "C:/Users/aravi/Desktop/keelAPIautomation/logo.svg",
    "orgName": "Image"
    }
        
    data7={
    "packageName":"Business analyst intern",
    "packageDescription":"The Business Analysis is a comprehensive platform that streamlines the recruitment process, allowing employers to post job openings, review applications, and schedule interviews."
    }
    
    data8={
    "packageId":1,
    "featureName":"Add Employee",
    "featureDescription":"Add Employee in order to proceed the process"
    }
    def modifyJsonfile(logopath):
        with open("loads.json", 'r') as json_file:
            data = json.load(json_file)

        data["logoPath"] = logopath

        with open("loads.json", 'w') as json_file:
            json_file.write("\n")
            json.dump(data, json_file, indent=4)
    
    def generate_random_name(length=5):
        random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return random_name
    
    def generate_random_email(length=6):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        email = random_string + "@mailinator.com"
        return email
    
    def generete_random_number():
        random_num = random.randint(1, 250)
        return random_num
    
    def generate_data():
        name = randomdata.generate_random_name()
        name1 = randomdata.generate_random_name()
        name2 = randomdata.generate_random_name()
        email = randomdata.generate_random_email()
        num = randomdata.generete_random_number()
        
        data4 = {
            "designation": ["CEO", name]
        }
        with open("load1.json", "w") as file:
            json.dump(data4, file, indent=4)

        data5 = {
            "roleName": name1,
            "roleShotName": name2,
            "permissionNo": num,
            "roleDesceiption": "Can able change all of his own data"
        }
        with open("load2.json", "w") as file:
            json.dump(data5, file, indent=4)
            
        bdata = {
            "organizationName": name,
            "subDomain": name1,
            "companyCategory": "IT",
            "logoPath": "https://hrms-poc.s3.eu-west-1.amazonaws.com/test-company2.svg",
            "active": True,
            "orgAddress": "dfdfsdf",
            "orgPincode": "34545",
            "orgCountry": 9,
            "orgState": None,
            "orgCity": None,
            "primary": {
                "firstName": "ram",
                "lastName": "kumar",
                "phone": "+91333543245",
                "designation": "CEO",
                "role": 1,
                "email": email,
                "address": "123 Main Street",
                "country": num,
                "state": None,
                "city": None,
                "pincode": "641006",
                "isPrimary": 1
            },
            "packages": [
                1
            ]
        }
        
        with open("loads.json", "w") as file:
            file.write("\n")
            json.dump(bdata, file, indent=4)