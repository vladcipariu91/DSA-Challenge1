import hashlib
from datetime import datetime, timezone


# Helper function to generate the timestamp
def timestamp_now():
    return str(datetime.utcnow().replace(tzinfo=timezone.utc))


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (self.timestamp + self.data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return "Block: [\ntimestamp: {},\ndata: {},\nhash: {},\nprev_hash: {}\n]" \
            .format(self.timestamp, self.data, self.hash, self.previous_hash)


class Blockchain:

    def __init__(self):
        self.head = Block(timestamp_now(), "Genesis Block", None)
        self.blocks = {self.head.hash: self.head}

    def add_block(self, data):
        new_block = Block(timestamp_now(), data, self.head.hash)
        self.blocks[new_block.hash] = new_block
        self.head = new_block

    def find(self, value, timestamp):
        search_block = Block(timestamp, value, None)
        return self.blocks.get(search_block.hash)

    def __repr__(self):
        current = self.head
        result = ""
        while current:
            result += str(current) + "\n"
            current = self.blocks.get(current.previous_hash)

        return result


blockchain = Blockchain()
genesis_timestamp = blockchain.head.timestamp
blockchain.add_block("Test 1")
blockchain.add_block("Test 2")
blockchain.add_block("Test 3")

block = blockchain.find("Genesis Block", genesis_timestamp)
print(block)
"""
expected:
Block: [
timestamp: 2019-10-09 16:56:03.187107+00:00,
data: Genesis Block,
hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
prev_hash: None
]
"""
block = blockchain.find("Genesis Block", timestamp_now())
print(block)
# expected: None
