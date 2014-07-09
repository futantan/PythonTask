class Student(object):
    def __init__(self, name, birth=None, phone_number=0, email=""):
        self.name = name
        self.birth = birth
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return "[\nname:" + self.name + "\nbirth:" + self.birth + "\nphoneNumber:" + str(
            self.phone_number) + "\nemail:" + self.email + "\n]"