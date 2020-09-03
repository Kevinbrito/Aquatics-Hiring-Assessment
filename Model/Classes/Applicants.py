import random


def create_custom(first_name, last_name):
    ret_val = first_name[0]
    for index in range(5):
        ret_val += str(random.randint(0, 9))
    ret_val += last_name[0]
    return ret_val


class Applicant:
    def __init__(self, first_name, last_name, email_address):
        self.firstName = first_name
        self.lastName = last_name
        self.custom_id = create_custom(first_name, last_name)
        self.email_address = email_address
        self.points = 0
