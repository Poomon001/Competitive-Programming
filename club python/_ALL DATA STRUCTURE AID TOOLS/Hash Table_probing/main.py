class HashTable:
    def __init__(self):
        self.Max = 20 # size of the list
        # self.arr = [None for i in range(self.Max)]
        self.arr = {} # this will initiate an empty list per each index to handle collision
        for i in range(self.Max):
            self.arr[i] = None

    def get_hash(self, value):
        index = 0
        for char in value:
            index += ord(char)
        return index%self.Max

    ''' Linear probing: index = (h(k) + i)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
    ''' if a slot is full, move to the next slot '''
    def insert_M1(self, value):
        # Get the hash value of the string and start the search at that index.
        i = self.get_hash(value)
        m = self.Max

        ''' Linear probing: index = (h(k) + i)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
        ''' if a slot is full, move to the next slot '''
        # loop until find the target or otherwise null
        while self.arr[i] is not None and self.arr[i] != "-1":
            i += 1
            # reach the end of the array. reset i
            if(i >= m):
                i = i%m

        self.arr[i] = value
        return i

    ''' quadratic probing: index = (h(k) + i^2)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
    ''' if a slot is full, move to the next i^2 slot '''
    def insert_M2(self, value):
        # Get the hash value of the string and start the search at that index.
        i = self.get_hash(value)
        m = self.Max

        # loop until find the target or otherwise null
        loopCounter = 1
        index = i
        while self.arr[index] is not None and self.arr[index] != "-1":
            pow = loopCounter ** 2
            loopCounter += 1
            index = i + pow

            # reach the end of the array. reset i
            if index >= m:
                index = index%m

        i = index

        self.arr[i] = value
        return i

    ''' Linear probing: index = (h(k) + i)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
    ''' if a slot is full, move to the next slot '''
    def find_M1(self, value):
        i = self.get_hash(value)
        m = self.Max

        # loop until find the target or otherwise null
        while self.arr[i] is not None and self.arr[i] != value:
            i += 1
            # reach the end of the array. reset i
            if i >= m:
                i = i % m

        # if get into null, then target doesn't exist
        if self.arr[i] is None:
            return -1

        return i

    ''' quadratic probing: index = (h(k) + i^2)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
    ''' if a slot is full, move to the next i^2 slot '''
    def find_M2(self, value):
        i = self.get_hash(value)
        m = self.Max

        # loop until find the target or otherwise null
        loopCounter = 1
        index = i
        while self.arr[index] is not None and self.arr[index] != value:
            pow = loopCounter ** 2
            loopCounter += 1
            index = i + pow

            # reach the end of the array. reset i
            if (index >= m):
                index = index % m

        i = index

        # if get into null, then target doesn't exist
        if self.arr[i] is None:
            return -1

        return i


    def delete(self, key, method):
        ''' Linear probing: index = (h(k) + i)%m where i is # of full slot that meets so far, h(k) = hash value, m = total slot '''
        ''' if a slot is full, move to the next slot '''
        # loop until find the target or otherwise null
        i = self.find_M1(key) if method == "M1" else self.find_M2(key)

        if i == -1:
            return -1

        self.arr[i] = "-1"
        return i

if __name__ == '__main__':
    print("\n+=== Linear Probing ===+\n")
    h1 = HashTable()
    h1.insert_M1("kk")
    h1.insert_M1("bt")
    h1.insert_M1("tb")
    h1.insert_M1("ua")

    print(h1.find_M1("kk"))
    print(h1.find_M1("bt"))
    print(h1.find_M1("tb"))
    print(h1.find_M1("xxxx"))
    print(h1.find_M1("ua"))

    h1.delete("tb", "M1")
    print(h1.find_M1("tb"))

    h1.insert_M1("tb")
    print(h1.find_M1("tb"))


    print("\n+=== Quadratic Probing ===+\n")
    h2 = HashTable()
    h2.insert_M2("kk")
    h2.insert_M2("bt")
    h2.insert_M2("tb")
    h2.insert_M2("ua")

    print(h2.find_M2("kk"))
    print(h2.find_M2("bt"))
    print(h2.find_M2("tb"))
    print(h2.find_M2("xxxx"))
    print(h2.find_M2("ua"))

    h2.delete("tb", "M2")
    print(h2.find_M2("tb"))

    h2.insert_M2("tb")
    print(h2.find_M2("tb"))


