class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, weight, special_notes, depature, status, delivery_time, truck_num):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.departure = depature
        self.status = status
        self.delivery_time = delivery_time
        self.truck_num = 0

        # If no special notes, pass string indicating no notes ("No Special Notes")
        if special_notes == '':
            self.special_notes = "No Special Notes"

        if status == None: 
            self.status = 'No status'
        
        if delivery_time == None: 
            self.status = 'NOT DELIVERED'

    # Attribution: https://www.digitalocean.com/community/tutorials/python-str-repr-functions
    def __str__(self):
        return f'{self.id}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.deadline}, {self.weight}, {self.special_notes}, {self.departure}, {self.status}, {self.delivery_time}, {self.truck_num}'
    