'''
title           : blockchain.py
description     : A blockchain implemenation in Python
author          : Computing&Coding
date_created    : 20211229
date_modified   : 20211229
version         : 0.1
usage           : python blockchain.py
python_version  : 3.6.2
'''
from datetime import datetime
from hashlib import sha256
import json
from flask import Flask, jsonify, request, render_template

nonce = 0

class Block:
  def __init__(self, transactions, previous_hash, nonce=0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
  def generate_hash(self):
    block_data = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_data.encode())
    return block_hash.hexdigest()

  def print_block(self):
    # prints block contents
     print("timestamp:", self.timestamp)
     print("transactions:", self.transactions)
     print("current hash:", self.hash)
new_transactions = {'sender_address': "0c39eb0fcfe74c009dfc8838", 
                    'recipient_address': "0c8a237b498327f499dfc8838afc5",
                    'value': "100"}
First_Block=Block(new_transactions,0)
First_Block.print_block()
