class Package:
    def __init__(self, id, address, city, zip, deadline, status, delivery_time):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.status = status
        self.delivery_time = delivery_time

    # Attribution: https://www.digitalocean.com/community/tutorials/python-str-repr-functions
    def __str__(self):
        return f'{self.id}, {self.address}, {self.city}, {self.zip}, 
        {self.deadline}, {self.status}, {self.delivery_time}'