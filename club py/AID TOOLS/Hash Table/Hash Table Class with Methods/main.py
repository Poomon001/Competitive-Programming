class HashTable:
    def __init__(self):
        self.Max = 10 # size of the list
        # self.arr = [None for i in range(self.Max)]
        self.arr = [[] for i in range(self.Max)] # this will initiate an empty list per each index to handle collision

    def get_hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index%self.Max

    def __setitem__(self, key, value):
        index = self.get_hash(key)

        # duplicate key then we update to the new tuple (cannot only change the key because it is a tuple element)
        if(len(self.arr[index]) > 0):
            for i in range(0, len(self.arr[index])):
                # duplicate key
                if(self.arr[index][i][0] == key):
                    self.arr[index][i] = (key, value)

                    # found duplicate and completed to update it
                    return

        # duplicate first or index then we append to the next element
        self.arr[index].append((key, value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        for ele in self.arr[index]:

            # find the key to return value
            if (ele[0] == key):
                return ele[1]

    def __delitem__(self, key):
        index = self.get_hash(key)
        for i in range(0, len(self.arr[index])):

            if(key == self.arr[index][i][0]):
                del self.arr[index][i]

if __name__ == '__main__':
    h1 = HashTable()
    h1["monday"] = 20
    h1["tuesday"] = 90
    h1["wednesday"] = 11
    h1["wednesday"] = 12
    h1["thursday"] = 13
    h1["friday"] = 3
    h1["saturday"] = 30
    print("Hash number:", h1.get_hash("monday"))
    print("Hash number:", h1.get_hash("tuesday"))
    print("Hash number:", h1.get_hash("wednesday"))
    print("Hash number:", h1.get_hash("thursday"))
    print("Hash number:", h1.get_hash("friday"))
    print("Hash number:", h1.get_hash("saturday"))
    print(h1["thursday"])
    del h1["saturday"]
    del h1["monday"]
    del h1["october "]
    print(h1.arr)


