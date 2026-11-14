from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict,Optional, Annotated

class PatientData(BaseModel):
    name: Annotated[str,Field(max_length=50, title="name of the patient", descripiton ="add the name of the patient over here")]
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int =Field(gt=0,lt=100)
    weight: float=Field(gt=0,strict=True)
    height: int=1.93
    married: bool = False
    allergies: Optional[List[str]]= Field(max_length=5)
    contact_info: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains=['hdfc.com', 'bankalfalah.com']
        domain_name=value.split('@')[-1]
        

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round((self.weight)/(self.height**2),2)
        return bmi


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_info:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model 

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
        print(patient.bmi)
        print("Data updated successfully in the database!")
        

patient_data={"name": "Sameer Sheikh", "email":"sameersheikh2999@bankalfalah.com", "linkedin_url": "https://www.linkedin.com/in/sameerrsheikhh/", "age": 27, "weight":88.2,"married":True, "allergies":["peanuts","almonds"],"contact_info": {"email": "sameersheikh3999@bankalfalah.com", "contact":"03095274580"}}
# patient=PatientData(**patient_data)
patient_1=PatientData(**patient_data)
update_patient_data(patient_1)









 