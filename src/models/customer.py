class Customer:
    def __init__(self, id: int, first_name: str, last_name: str, country:str, credit_limit:float):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.credit_limit = credit_limit

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name}"