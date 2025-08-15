from typing import List
from collections import Counter
import heapq

'''
    Link: https://leetcode.com/problems/task-scheduler
    Purpose: Find the minimum number of intervals required to complete all tasks.
           : Each identical task need to wait until n intervals before repeating
    parameter: List[str] tasks - a list of tasks: namely A - Z.
             : int n - a number of waiting intervals before repeating tje same task
    return: int min_interval - the minimum number of intervals
    Pre-Condition: 1 <= tasks.length <= 10^4
                 : tasks[i] is an uppercase English letter.
                 : 0 <= n <= 100
    Post-Condition: none
'''
# runtime: O(nlogk), space: O(logk) where n = total number of task, k = 26 cenglish characters
def leastInterval_M1(tasks: List[str], n: int) -> int:
    # create max heap of x task ordered by freq
    char_to_freq = Counter(tasks)
    max_heap = [-count for count in char_to_freq.values()]  # keep trank of remaining task
    heapq.heapify(max_heap)

    cycle = n + 1  # e.g X, _, _, X where n = 2

    # iterate until no task remain: O(nlogk) where n = number of tasks, k = 26
    min_interval = 0
    while max_heap:
        temp = []
        for i in range(cycle):
            if max_heap:
                # can process n unique tasks per cycle
                min_interval += 1
                curr_task_count = -heapq.heappop(max_heap) - 1
                if curr_task_count > 0:
                    temp.append(curr_task_count)
            elif temp:
                # All unique tasks are process in this cycle, idle wait for the next cycle
                min_interval += 1

        for updated_task_count in temp:
            # push remaining uncompleted tasks back
            heapq.heappush(max_heap, -updated_task_count)

    return min_interval

'''
    Link: https://leetcode.com/problems/task-scheduler
    Purpose: Find the minimum number of intervals required to complete all tasks.
           : Each identical task need to wait until n intervals before repeating
    parameter: List[str] tasks - a list of tasks: namely A - Z.
             : int n - a number of waiting intervals before repeating tje same task
    return: int min_interval - the minimum number of intervals
    Pre-Condition: 1 <= tasks.length <= 10^4
                 : tasks[i] is an uppercase English letter.
                 : 0 <= n <= 100
    Post-Condition: none
'''
# runtime: O(n), space: O(k) where n = total number of task, k = 26 cenglish characters
def leastInterval_M2(tasks: List[str], n: int) -> int:
    # Key: schedule the most frequently task first to minimize the wait time
    #    : Greedy by filling all idle slots as much as possible to make the pocessing time closer to len(tasks)
    #    : If more total tasks than idle slots, add them at the end garantee no gap violation b/c we have worst case idle slots
    # e.g AAAABBBBCCCCDDDD, n = 2 = A, _, _, A, _, _, A, _, _, A
    # The worst case for each          B, _, _, B, _, _, B, _, _, B
    #                                     C, _, _, C, _, _, C, _, _, C
    #                                        D, _, _, D, _, _, D, _, _, D = ABCDABCDABCDABCD = len(s)
    task_to_count = Counter(tasks)
    max_freq = 0
    most_freq_task = ''
    for task, count in task_to_count.items():
        if count >= max_freq:
            max_freq = count
            most_freq_task = task

    max_idle_slots = (max_freq - 1) * n # A, _, _, A, _, _, A = 4 idle slots (worst case cannot alternate at all)

    # fill in idle slots
    for task, count in task_to_count.items():
        if task != most_freq_task:
            if count == max_freq:
                # A _ _ A _ _ A
                # A B _ A B _ A B with 3 Bs
                # The last B doesn't go into an idle slot, so added 1 back
                max_idle_slots -= (count - 1)
            else:
                max_idle_slots -= count

    # the Best-case processing time is len(tasks), but we may have some idle slots in between
    return max_idle_slots + len(tasks) if max_idle_slots > 0 else len(tasks)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(leastInterval_M1(["A", "A", "A", "B", "B", "B"], 1)) # 6
    print(leastInterval_M1(["A","A","A","B","B","B"], 2)) # 8
    print(leastInterval_M1(["A", "A", "A", "B", "B", "B"], 3)) # 10
    print(leastInterval_M1(["A","C","A","B","D","B"], 3)) # 6
    print(leastInterval_M1(["A", "C", "A", "B", "D", "B"], 3)) # 6
    print(leastInterval_M1(["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D"], 2)) # 14
    print(leastInterval_M1(["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D"], 4)) # 18

    print("\n === Solution 2 === \n")
    print(leastInterval_M2(["A", "A", "A", "B", "B", "B"], 1))  # 6
    print(leastInterval_M2(["A", "A", "A", "B", "B", "B"], 2))  # 8
    print(leastInterval_M2(["A", "A", "A", "B", "B", "B"], 3))  # 10
    print(leastInterval_M2(["A", "C", "A", "B", "D", "B"], 3))  # 6
    print(leastInterval_M2(["A", "C", "A", "B", "D", "B"], 3))  # 6
    print(leastInterval_M2(["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D"], 2))  # 14
    print(leastInterval_M2(["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D"], 4))  # 18

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
