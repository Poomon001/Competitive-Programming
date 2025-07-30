from typing import List

'''
    Link: https://leetcode.com/problems/task-scheduler-ii
    Purpose: Find the minimum number of days needed to complete all tasks, where
           : tasks[i] represents the type of the ith task
           : the same type needs to wait for space days
    parameter: List[int] tasks - a list of tasks
             : int space - a day need to wait before process the same task 
    return: int day - the minimum number of days needed to complete all tasks
    Pre-Condition: 1 <= tasks.length <= 10^5
                 : 1 <= tasks[i] <= 10^9
                 : 1 <= space <= tasks.length
    Post-Condition: none
'''
# hashmap: runtime: O(n), memnory: O(n)
def taskSchedulerII(tasks: List[int], space: int) -> int:
    task_to_avalible = {}
    day = 0

    for task in tasks:
        if task in task_to_avalible:
            avalible = task_to_avalible[task]
            if avalible > day:
                day = avalible

        task_to_avalible[task] = day + space + 1
        day += 1

    return day


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(taskSchedulerII([5,8,8,5], 2)) # 6
    print(taskSchedulerII([5, 8, 8, 5], 5)) # 9
    print(taskSchedulerII([1,2,1,2,3,1], 3)) # 9
    print(taskSchedulerII([1, 2, 3], 10)) # 3
    print(taskSchedulerII([1], 5)) # 1
    print(taskSchedulerII([1, 1, 1], 1)) # 5
