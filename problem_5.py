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
        if value is None or timestamp is None:
            return None

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
a_block = None
for i in range(0, 100):
    blockchain.add_block("Test {}".format(i))
    if i == 33:
        a_block = blockchain.head

before = datetime.now()
block = blockchain.find("Genesis Block", genesis_timestamp)
after = datetime.now()
print("It took {} to find the genesis block".format(after - before))
print(block)
"""
expected:
Block: [
timestamp: 2019-10-09 16:56:03.187107+00:00, // this will vary
data: Genesis Block,
hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
prev_hash: None
]
"""

block = blockchain.find("Genesis Block", timestamp_now())
print(block)
# expected: None

block = blockchain.find("Test 33", a_block.timestamp)
print(block)
"""
expected:
Block: [
timestamp: 2019-10-10 10:33:46.934075+00:00, // this will vary 
data: Test 33,
hash: c3dc8a00c2ec18e70becb81976332df1071cd091a254dee14388c5f0f4a1cf7c,
prev_hash: a40bd66484158ecf8ee95e16697519cc333cf80ac6e3500650567c5daa8a67a4
]
"""

block = blockchain.find(None, timestamp_now())
print(block)
# expected: None

block = blockchain.find(None, None)
print(block)
# expected: None
