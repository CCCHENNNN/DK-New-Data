import json

from block_header import BlockHeader
from transaction import Transaction
from block import Block
from blockchain import Blockchain


def read_header(header):
    # Implement these functions to help you
    # Takes a dictionary as an input
    # Exercise 4
    return BlockHeader(header["index"],header["previous_hash"],header["timestamp"],header["nonce"])
    pass

def read_transaction(transaction):
    # Same above for transformation
    # Exercise 8
    return Transaction(transaction["index"],transaction["sender"],transaction["receiver"],transaction["amount"])
    pass

def read_block(block):
    # Reads a block from a dictionary
    # Exercise 10
    header = read_header(block["header"])
    transactions = []
    for transaction in block["transactions"]:
        transactions.append(read_transaction(transaction))
    return Block(header, transactions)
    pass

def read_block_json(block_json):
    # Reads a block in json format
    # Exercise 10
    return json.loads(block_json)
    pass

def read_chain(chain):
    # read the chain from a json str
    # Returns a list of Block
    # This method does not do any checking
    # Exercise 20
    blocks = []
    for block in json.loads(chain):
        blocks.append(read_block(block))
    return blocks
    pass

# Exercise 11

# for i in range(0,10):
#     file = "blocks/block" + str(i) + ".json"
#     with open(file,'r') as load_f:
#         block = read_block(json.load(load_f))
#         print("The number of transactions in " + file + " is " + str(len(block.transactions)))
# with open("blocks/initial_block.json",'r') as load_f:
#     block = read_block(json.load(load_f))
#     print("The number of transactions in blocks/initial_block.json is " + str(len(block.transactions)))

# Exercise 18

# for i in range(0,10):
#     file = "blocks_to_prove/block" + str(i) + ".json"
#     with open(file,'r') as load_f:
#         block = read_block(json.load(load_f))
#         print("For the file " + file + " :")
#         block.make_proof_ready()

# Exercise 23

# for i in range(0,10):
#     block_chain = Blockchain()
#     file = "blockchain_wallets/chain" + str(i) + ".json"
#     with open(file,'r') as load_f:
#         for block in read_chain(load_f.read()):
#             block_chain.add_block(block)
#         print("For the file " + file + " :")
#         for (k,v) in block_chain.wallets.items():
#             print(k + ": " + str(v))

# Exercise 25

# for i in range(0,10):
#     file = "blockchain_incorrect/chain" + str(i) + ".json"
#     with open(file,'r') as load_f:
#         block_chain = Blockchain()
#         index_error = 0
#         print("For the file " + file + " :")
#         for block in read_chain(load_f.read()):
#             if not block_chain.add_block(block):
#                 print(" of the block " + str(index_error))
#                 break
#             else:
#                 index_error += 1



