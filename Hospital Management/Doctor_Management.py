import pandas as pd

# Function to add a new doctor
def add_doctor(name, specialization, phone):
    data = {
        'Name': [name],
        'Specialization': [specialization],
        'Phone': [phone]
    }
    df = pd.DataFrame(data)
    df.to_excel('doctors.xlsx', mode='a', index=False, header=False)

# Function to get all doctors
def get_all_doctors():
    df = pd.read_excel('doctors.xlsx')
    return df

# Function to search for a doctor by name
def search_doctor_by_name(name):
    df = pd.read_excel('doctors.xlsx')
    result = df[df['Name'].str.contains(name, case=False)]
    return result

# Add more functions for updating and deleting doctor records as needed.
