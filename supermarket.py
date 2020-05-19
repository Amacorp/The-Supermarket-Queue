# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
# 
# Input:
# customers: An integer array representing customer estimated processing times.
# tillCount: An integer representing available tills.
# 
# output:
# An integer representing the maximum time required to process all customers.
# 
# Examples:
# queueTime([5,3,4], 0) returns 12
# queueTime([10,2,3,3], 2) returns 10
# queueTime([2,3,10], 2) returns 12



def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

test = queue_time([2,2,3,3,4,4], 2)
print(test)


Test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
# Test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
# Test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
# Test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")
