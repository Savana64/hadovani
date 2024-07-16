import pickle
import os

# Function to create a full path for the file.
def create_path(file_name):
    # Get the directory of the current script.
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Return the full path.
    return os.path.join(script_dir, file_name)

# Function to serialize data and save it to a file.
def serialize(file_name, data):
    # Open the file in binary write mode and save the serialized data to it.
    with open(create_path(file_name), "wb") as file:
        pickle.dump(data, file)

# Function to load data from a file and deserialize it.
def deserialize(file_name):
    # Open the file in binary read mode, load and deserialize the data from it.
    with open(create_path(file_name), "rb") as file:
         data = pickle.load(file)
    return data

# Define a class for a person.
class Person:
    # Initialize a new instance of the class.
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    # Return the full name of the person.
    def get_full_name(self):
        return f"{self.name}{self.last_name}"

try:
    # Create a new Person instance.
    p = Person("Bill", "Gates")
    # Print the full name of the person.
    print(f"Original person:\n{p.get_full_name()}\n")

    # Define the file name.
    file_name = "person.dat"

    # Serialize the Person instance and write it to a file.
    serialize(file_name, p)
    # Read the file, deserialize its content and store it in 'person_restored'.
    person_restored = deserialize(file_name)

    # Print the full name of the deserialized Person instance.
    print(f"Deserialized person:\n{person_restored.get_full_name()}\n ten čurák")

# Handle any exceptions that might occur during the process.
except Exception as e:
    print(e)