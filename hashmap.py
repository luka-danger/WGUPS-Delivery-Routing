# Attribution: WGU Webinar 1: "Let's Go Hashing"
# Link: https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
class HashMap:
    # Create 40 bucket hash table 
    # Could reduce size to 10 and create chaining to prevent collisions 
    # For relevatively small amount of data, 40 buckets will suffice
    # One bucket per element allows for O(1) for methods 
    def __init__(self, initial_size = 40):
        # Create empty buckets
        self.hashlist = []
        # Append empty buckets to a list
        for i in range(initial_size):
            self.hashlist.append([])

    # Time-Complexity: O(n)
    # Allows for hash function reusability 
    def get_bucket(self, key):
        # Hash Function: Assign each item to a bucket
        bucket = hash(key) % len(self.hashlist)
        # Store item in list
        bucket_list = self.hashlist[bucket]
        return bucket_list
    
    # Time-Complexity: O(1)
    # Insert key, value pair into hash map
    def insert(self, key, value):
        bucket_list = self.get_bucket(int(key))

        # Update key / value pair if key already in bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True
        # Append value to bucket_list if key not in bucket_list
        key_value = [int(key), value]
        bucket_list.append(key_value)
        return True
    
    # Time-Complexity: O(1)
    # Search for element in hashmap by key
    def lookup(self, key):
        bucket_list = self.get_bucket(key)

        # Search key and return value pair 
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return 'Package ID not found.' 

    # Time-Complexity: O(1)
    # Remove element from hashmap
    def remove(self, key):
        bucket_list = self.get_bucket(key)

        # Remove key / value pair from bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value[0], key_value[1])

        