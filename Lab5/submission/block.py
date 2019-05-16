import json
import hashlib
from block_header import BlockHeader


class Block(object):

    def __init__(self, header, transactions):
        # Store everything internally
        # header is a BlockHeader and transaction is a list of Transaction
        # Exercise 9
        self.N_STARTING_ZEROS = 4
        self.header = header
        self.transactions = transactions #list
        pass

    def to_dict(self):
        # Turns the object into a dictionary
        # There are two fields: header and transactions
        # The values are obtained by using the to_dict methods
        # Exercise 9
        block_dict = {}
        block_dict["header"] = self.header
        block_dict["transactions"] = self.transactions
        return block_dict
        pass

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        # Exercise 9
        return json.dumps(self.to_dict(), sort_key=True)
        pass

    def is_proof_ready(self):
        # Check whether the block is proven
        # For that, make sure the hash begins by N_STARTING_ZEROS
        # Exercise 17
        start_zeros = ""
        for i in range(0,self.N_STARTING_ZEROS):
            start_zeros += '0'
        if self.header.get_hash().startswith(start_zeros):
            return True
        else:
            return False
        pass


    def make_proof_ready(self):
        # Transforms the block into a proven block
        # Exercise 17
        nonce = 0
        while not self.is_proof_ready():
            nonce += 1
            self.header.set_nonce(nonce)
        print("The nonce is: " + str(nonce))
        print("The hash value is: " + self.header.get_hash())
        pass


    




