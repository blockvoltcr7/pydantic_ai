from pydantic import BaseModel


class User(BaseModel):
    """A class representing a user with a name and age."""

    name: str  # The name of the user
    age: int  # The age of the user


# Create an instance of the User class
user = User(name="John", age=30)

# Print the user object
print(user)

# Print the string representation of the user object
print(str(user))

# Dump the model's data as a dictionary
print(user.model_dump())

# Dump the model's data as a JSON string
print(user.model_dump_json())

# Access the model's fields
print(user.model_fields)
