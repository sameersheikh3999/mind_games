def add_patient_data(name:str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Data added successfully to the database!")
    else:
        raise TypeError("Invalid data type for name or age. Name should be a string")


add_patient_data("Sameer","27")

