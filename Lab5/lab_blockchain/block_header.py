import json
import hashlib


class BlockHeader(object):

    def __init__(self, index, previous_hash, timestamp, nonce):
        # Store internally
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce
        pass

    def to_dict(self):
        # Transform object into a dictionary for future transformation in JSON
        # The gave of the fields are the name of the variables
        head_dict = {}
        head_dict["index"] = self.index
        head_dict["previous_hash"] = self.previous_hash
        head_dict["timestamp"] = self.timestamp
        head_dict["nonce"] = self.nonce 
        return head_dict
        pass

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        return json.dumps(self.to_dict(), sort_keys=True)
        pass

    def set_nonce(self, new_nonce):
        # Set the nonce value
        # Exercise 13
        self.nonce = new_nonce
        pass

    def get_hash(self):
        # Use hashlib to hash the block using sha256
        # Use hexdigest to get a string result
        # Exercise 14
        sha256 = hashlib.sha256()
        sha256.update(self.to_json().encode('utf-8'))
        res = sha256.hexdigest()
        return res
        pass

