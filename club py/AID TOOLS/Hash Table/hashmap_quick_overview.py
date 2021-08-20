input = '''
monday: 101.0,
tuesday: 89.0,
wednesday: 100.0,
thursday: 111.1,
friday: 103.0,
saturday: 0.0,
sunday: 0.0
'''

''' Dictionay is an implimentation of hash table '''
def create_dictionay(line):
    dic = {}
    line = input.split(",")
    for l in line:
        l = l.strip()
        tokens = l.split(":")
        key = tokens[0]
        value = tokens[1]
        dic[key] = value
    return dic

dic = create_dictionay(input)
print(dic["friday"])

''' hash map '''
''' if an array is a collection of data that needs int index to access '''
''' hashmap is a collection of data that can be accessed by non-int index type eg. string or char '''
''' we need hash function to convert non-int index type into int '''

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)

    # this will generate int index between 0 to 99 (size of the list)
    return h % 100

print(get_hash("monday"))