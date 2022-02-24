class Patient:
    # Initialize and accept argument for each attribute
    def __init__(self, patientID, name, address, phone, veteran_status):
        self.__patientID = patientID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status

    # Accessor methods to return each attribute
    def get_patientID(self):
        return self.__patientID

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_veteran_status(self):
        return self.__veteran_status
