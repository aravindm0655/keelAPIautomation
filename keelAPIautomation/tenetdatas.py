import random
import string
import json

class RandomData:
    data1 = {
        "userName": "pavansmash1@mailinator.com",
        "password": "Balaji@123"
    }

    datax={
    "relationType":7 ,
    "employeeId": 129,
    "firstName": "sasi",
    "lastName": "sasi",
    "gender": 1,
    "dob": "1999-07-21"

    }
    data8={
        "relationType":1 ,
        "firstName": "sasiaa",
        "lastName": "sasi",
        "gender": 1,
        "dob": "1999-07-21"
        
        }
    data12={
    "employeeuuid": "23f52efa-70d2-4a14-b9b1-5c591d1acf0c",
    }
    file1 = {
    'profileImage': ('profile.jpg', open("C:/Users/aravi/Desktop/keelAPIautomation/profile.JPG", 'rb'), 'image/jpeg')
    }
    
    data17={
    "employeeuuid": "23f52efa-70d2-4a14-b9b1-5c591d1acf0c",
    "document_type": "paySlip",
    }
    file2 = {
    'documentFile': ('profile.jpg', open("C:/Users/aravi/Desktop/keelAPIautomation/profile.JPG", 'rb'), 'image/jpeg')
    }
    
    data18={
    "employeeuuid": "23f52efa-70d2-4a14-b9b1-5c591d1acf0c",
    }
    file3={
        "identificationFiles": ('profile.jpg', open("C:/Users/aravi/Desktop/keelAPIautomation/profile.JPG", 'rb'), 'image/jpeg'),
    }
    file4={
        "documentFiles": ('profile.jpg', open("C:/Users/aravi/Desktop/keelAPIautomation/profile.JPG", 'rb'), 'image/jpeg'),
    }
    
    data13={
        "proofType": 2,
        "employeeId": 129,
        "proofIdNumber": "AAAAA0000A",
        "url": [
            {
                "fileName": "ti.jpeg.pdf",
                "format": "pdf",
                "url": "https://hrms-poc.s3.eu-west-1.amazonaws.com/organizationId-100/UUID-944e11bf-ca76-4882-a437-74cd19ed5d76/ identification/ti.jpeg.pdf",
                "fileSize":"5.0 MB"

            },
            {
                "fileName": "tiger-jpg.pdf",
                "format": "pdf",
                "url": "https://hrms-poc.s3.eu-west-1.amazonaws.com/organizationId-100/UUID-944e11bf-ca76-4882-a437-74cd19ed5d76/ identification/tiger-jpg.pdf",
                "fileSize":"0.23 MB"
            }
        ]
    }
    data14={

        "uuid": "23f52efa-70d2-4a14-b9b1-5c591d1acf0c"

    }
    data15={
        "employee_id": 129,
        "is_active": True
    }
    data16={
        "firstName": "kb",
        "lastName": "pavan",
        "officialEmail": "pavankumar@mailinator.com",
        "companyUserId": "TS030",
        "designation": 97,
        "role": 607,
        "reportingManager": 373,
        "userStatus": 1,
        "workLocation": None,
        "joiningDate": None,
        "bgvCompletionDate": None
    }
    @staticmethod
    def generate_random_name(length=5):
        random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return random_name

    @staticmethod
    def generate_random_email(length=6):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        email = random_string + "@mailinator.com"
        return email

    @staticmethod
    def generate_data():
        name = RandomData.generate_random_name()
        global name1
        name1 = RandomData.generate_random_name()
        email = RandomData.generate_random_email()
        
        data2 = {
            "firstName": "ashok",
            "lastName": "kumar",  
            "officialEmail": email,
            "designation": 95,
            "reportingManager": 129,  #retrive first
            "role": 95,   #retrive first
            "workLocation": 91,
            "joiningDate":"2000-02-02",
            "employeeId": name,
            "userStatus": 1
        }
        with open("data2.json", "w") as file:
                json.dump(data2, file, indent=4) 
        data3={
            "designation": [name1]
        }
        with open("data3.json", "w") as file:
            json.dump(data3, file, indent=4) 
        data5={
            "eductionType" : [name,name1]
        }
        with open("data5.json", "w") as file:
            json.dump(data5, file, indent=4) 
        data6={
            "genderType" : [name]
        }
        with open("data6.json", "w") as file:
            json.dump(data6, file, indent=4) 
        data11={
            "proofType" : [name1]
        }
        with open("data11.json", "w") as file:
            json.dump(data11, file, indent=4) 