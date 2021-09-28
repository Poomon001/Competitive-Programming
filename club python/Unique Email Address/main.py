from typing import List

'''
    Link: https://leetcode.com/problems/unique-email-addresses/
    Purpose: Find the number of different addresses.
           : 1. Every valid email consists of a local name and a domain name, separated by the '@' sign.
           : 2. If you add periods '.' between some characters in the local name part of an email address,
            mail sent there will be forwarded to the same address without dots in the local name.
           : 3. If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
    parameter: List[str] - a list of all emails
    return: int - the number of different addresses.
    Pre-Condition: 1 <= emails.length <= 100
                 : 1 <= emails[i].length <= 100
                 : email[i] consist of lowercase English letters, '+', '.' and '@'.
                 : Each emails[i] contains exactly one '@' character.   
                 : All local and domain names are non-empty.
                 : Local names do not start with a '+' character.
    Post-Condition: none
'''

# simplify the email into the form without "." or "+" - runtime: O(n^2), memory: O(n)
def numUniqueEmails(emails: List[str]) -> int:
    uniqueEmails = []
    for email in emails:
        # get local name = name[0]
        # get domain name = name[1]
        name = email.split("@")

        # simplify the local name
        localName = ""
        for char in name[0]:
            if char == '.':
                continue
            elif char == '+':
                break
            else:
                localName += char

        # save the result
        email = localName+"@"+name[1]
        if email not in uniqueEmails:
           uniqueEmails.append(email)

    return len(uniqueEmails)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails)) # 2

    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    print(numUniqueEmails(emails)) # 3

    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print(numUniqueEmails(emails)) # 2

