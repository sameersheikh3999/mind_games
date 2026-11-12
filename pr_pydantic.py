from pydantic import BaseModel

class PatientData(BaseModel):
    name: str  
    age: int

    def add_patient_data(patient: PatientData)
        pass

    patient_data={"name": "Sameer", "age": 27}
    print("I hope I have added something in the repository")
