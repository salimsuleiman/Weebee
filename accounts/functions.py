from random import randint
from django.utils.crypto import get_random_string




def create_customer_instant(data, Customer):
   return  Customer(
            firstName = data['firstName'],
            lastName = data['lastName'],
            phoneNumber = data['phoneNumber'],
            dateOfBirth = data['dateOfBirth'],
            middleName = data['middleName'],
            address = data['address'],
            state = data['state'],
            idCardNumber = data['idCardNumber'],
            stateOfOrigin = data['stateOfOrigin'],
            gender = data['gender'],
            email = data['email'],
        )

  



def generate_account_number():
    random_str = get_random_string(11, allowed_chars='01234567890987654321')
    return int(random_str)