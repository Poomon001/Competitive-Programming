from typing import List

'''
    Link: https://leetcode.com/problems/encode-and-decode-strings/
    Purpose: Design an algorithm to encode a list of strings to a string. 
           : to decoded back to the original list of strings.
    parameter: str strs - a list of strings
             : str s - an encoded string 
    return: str strs - a list of strings
          : str s - an encoded string 
    Pre-Condition: 1 <= strs.length <= 200
                 : 10 <= strs[i].length <= 200
                 : strs[i] contains any possible characters out of 256 valid ASCII characters.
    Post-Condition: none
'''
class NetworkTransferEncoding:
    @staticmethod
    def encode(strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        for i in range(len(strs)):
            s = strs[i]
            encode = str(len(s)) + "/" + s
            strs[i] = encode
        return "".join(strs)

    @staticmethod
    def decode(s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '/':
                # get the length
                j += 1
            length = int(s[i:j])
            i = j + 1

            strs.append(s[i: i + length])
            i = i + length
        return strs

class EscapeEncoding:
    @staticmethod
    def encode(strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        for i in range(len(strs)):
            s = strs[i]
            # word breaker cannot be "/" because it gets index out of bound
            # e.g hello/world/ -> "world" cant be added b.c i is at '/' and j is out of bound
            encode = s.replace("/", "//") + "/:"
            strs[i] = encode
        return "".join(strs)

    @staticmethod
    def decode(s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []
        sub_strs = ""
        i = 0
        while i < len(s):
            if s[i] == "/" and s[i+1] == ":":
                # ending of word case
                strs.append(sub_strs)
                sub_strs = ""
                i += 2
            elif s[i] == "/" and s[i+1] == "/":
                # escaped char case
                sub_strs += s[i]
                i += 2
            else:
                # regular char case
                sub_strs += s[i]
                i += 1
        return strs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = NetworkTransferEncoding
    print("\n=== solution 1 encode ===\n")
    print(t.encode(["Hello","World"])) # 5/Hello5/World
    print(t.encode([""])) # 0/
    print(t.encode(["Hello","World/6//","hi"])) # 5/Hello9/World/6//2/hi
    print(t.encode(["H"])) # 1/H
    print(t.encode(["",""])) # 0/0/
    print(t.encode(["/"])) # 1//
    print(t.encode(["Hello","World/6/:/:","6/:hi"])) # 5/Hello11/World/6/:/:5/6/:hi

    print("\n=== solution 1 decode ===\n")
    print(t.decode(t.encode([""]))) # ['']
    print(t.decode(t.encode(["Hello","World/6//","hi"]))) # ['Hello', 'World/6//', 'hi']
    print(t.decode(t.encode(["H"]))) # ['H']
    print(t.decode(t.encode(["",""]))) # ['', '']
    print(t.decode(t.encode(["/"]))) # ['/']
    print(t.decode(t.encode(["Hello","World/6/:/:","6/:hi"]))) # ['Hello', 'World/6/:/:', '6/:hi']

    e = EscapeEncoding
    print("\n=== solution 2 encode ===\n")
    print(e.encode(["Hello", "World"]))  # Hello/:World/:
    print(e.encode([""]))  # /:
    print(e.encode(["Hello", "World/6//", "hi"]))  # Hello/:World//6/////:hi/:
    print(e.encode(["H"]))  # H/:
    print(e.encode(["", ""]))  # /:/:
    print(e.encode(["/"]))  # ///:
    print(e.encode(["Hello", "World/6/:/:", "6/:hi"]))  # Hello/:World//6//://:/:6//:hi/:

    print("\n=== solution 2 decode ===\n")
    print(e.decode(e.encode([""])))  # ['']
    print(e.decode(e.encode(["Hello", "World/6//", "hi"])))  # ['Hello', 'World/6//', 'hi']
    print(e.decode(e.encode(["H"])))  # ['H']
    print(e.decode(e.encode(["", ""])))  # ['', '']
    print(e.decode(e.encode(["/"])))  # ['/']
    print(e.decode(e.encode(["Hello", "World/6/:/:", "6/:hi"])))  # ['Hello', 'World/6/:/:', '6/:hi']


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
