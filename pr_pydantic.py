from pydantic import BaseModel

class PatientData(BaseModel):
    name: str  
    age: int

def add_patient_data(patient: PatientData):
        print(patient.name)
        print(patient.age)
        print("Data added successfully")
        
def update_patient_data(patient: PatientData):
        print(patient.name)
        print(patient.age)
        print("Data updated successfully in the database!")
        

patient_data={"name": "Sameer", "age": 27}
# patient=PatientData(**patient_data)
patient_1=PatientData(**patient_data)


update_patient_data(patient_1)


 