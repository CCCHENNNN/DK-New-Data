class Transaction(object):

    def __init__(self, index, sender, receiver, amount):
        # Store internally
        # Exercise 6
        self.index = index
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        pass

    def to_dict(self):
        # Transform object into a dictionary for future transformation in JSON
        # The gave of the fields are the name of the variables
        # Exercise 6
        tran_dict = {}
        tran_dict["index"] = self.index
        tran_dict["sender"] = self.sender
        tran_dict["receiver"] = self.receiver
        tran_dict["amount"] = self.amount 
        return tran_dict
        pass
