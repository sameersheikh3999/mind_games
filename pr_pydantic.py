from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict,Optional

class PatientData(BaseModel):
    name: str 
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int
    weight: float 
    married: bool = False
    allergies: Optional[List[str]]= None
    contact_info: Dict[str,str]

def add_patient_data(patient: PatientData):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print("Data added successfully")
        
def update_patient_data(patient: PatientData):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_info)
        print("Data updated successfully in the database!")
        

patient_data={"name": "Sameer", "email":"sameersheikh2999@gmail.com", "linkedin_url": "https://www.linkedin.com/in/sameerrsheikhh/", "age": 27, "weight":70.5,"married":True, "allergies":["peanuts","almonds"],"contact_info": {"email": "sameersheikh3999@gmail.com", "contact":"03095274580"}}
# patient=PatientData(**patient_data)
patient_1=PatientData(**patient_data)
update_patient_data(patient_1)









 