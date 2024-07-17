# Attribution: WGU Webinar 1: "Let's Go Hashing"
class HashMap:
    # Create 10 bucket hash table 
    def __init__(self, initial_size = 10):
        # Create empty buckets
        self.hashlist = []
        # Append empty buckets to a list
        for i in range(initial_size):
            self.hashlist.append([])

    def insert(self, key, value):
        # Hash Function: Assign each item to a bucket
        bucket = hash(value) % len(self.hashtable)
        # Store item in list
        bucket_list = self.hashlist[bucket]

        # Update key / value pair if key already in bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value 
                return True
        # Append value to bucket_list if key not in bucket_list
        key_value = [key, value]
        bucket_list.append(key_value)
        return True
                


        