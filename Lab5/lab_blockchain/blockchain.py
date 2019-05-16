class Blockchain(object):

    def __init__(self):
        self.chain = [] # contains the blockchain
        self.wallets = dict() # Contains the amount of coin each user owns
        self.wallets["admin"] = 100000000000000

    def add_block(self, block):
        # Add a block to the chain
        # It needs to check if a block is correct
        # Returns True if the block was added, False otherwise
        # Exercise 22
        if block.is_proof_ready() and self.check_legal_transactions(block):
            self.chain.append(block)
            self.update_wallet(block)
            return True
        else:
            return False
        pass

    def update_wallet(self, block):
        # Update the values in the wallet
        # We assume the block is correct
        # Exercise 21
        for transaction in block.transactions:
            sender = transaction.sender
            receiver = transaction.receiver
            amount = transaction.amount
            if receiver in self.wallets:
                self.wallets[receiver] += amount
            else:
                self.wallets[receiver] = amount
            if sender in self.wallets:
                self.wallets[sender] -= amount
        pass

    def check_legal_transactions(self, block):
        # Check if the transactions of a block are legal given the current state
        # of the chain and the wallet
        # Returns a boolean
        # Exercise 24
        is_first = True
        for transaction in block.transactions:
            sender = transaction.sender
            receiver = transaction.receiver
            amount = transaction.amount
            if sender not in self.wallets:
                if is_first:
                    print("The index of the first incorrect transaction is : " + str(transaction.index), end = "")
                    is_first = False
                return False
            elif (self.wallets[sender] - amount) < 0:
                if is_first:
                    print("The index of the first incorrect is in the transaction " + str(transaction.index), end = "")
                    is_first = False
                return False
        return True
        pass

