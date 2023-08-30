import random
import string
import json

class RandomData:
    data1 = {
        "userName": "pavansmash1@mailinator.com",
        "password": "Balaji@123"
    }


    data7={
    "employeeuuid": "23f52efa-70d2-4a14-b9b1-5c591d1acf0c",
    "profileImage":"C:/Users/aravi/Desktop/keelAPIautomation/RZFZ7102.JPG"
    }
    data8={
        "relationType":1 ,
        "firstName": "sasi",
        "lastName": "sasi",
        "gender": 2,
        "dob": "1999-07-21"
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
        name1 = RandomData.generate_random_name()
        email = RandomData.generate_random_email()
        data2 = {
            "firstName": "ashok",
            "lastName": "kumar",  
            "officialEmail": email,
            "designation": 95,
            "reportingManager": 129,  #retrive first
            "role": 95,   #retrive first
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