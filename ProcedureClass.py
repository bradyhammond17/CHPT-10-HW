class Procedure:
    # Initialize and accept argument for each attribute
    def __init__(self, procedure, date, practitioner, charges, patID):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges
        self.__patID = patID

    # Accessor methods to return each attribute
    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def get_patID(self):
        return self.__patID
