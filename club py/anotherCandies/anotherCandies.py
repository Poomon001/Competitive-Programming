numCase = int(input())

for x in range(numCase):
       sum = 0
       Blank = input()
       numChild = int(input())
       for y in range(numChild):
           numCandies = int(input())
           sum += numCandies
       if sum%numChild == 0:
           print("YES")
       else:
           print("NO")

