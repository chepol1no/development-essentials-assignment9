# Task 2.1. Lists: ordered, mutable collections with duplicates.

numbers = [10, 20, 30, 20]
print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice:", numbers[1:3])

numbers.append(40)
print("After append:", numbers)

numbers.extend([50, 60])
print("After extend:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)
  
numbers.remove(20)
print("After removing the first 20:", numbers)

removed = numbers.pop()
print("Popped element:", removed)
print("After pop:", numbers)

numbers[0] = 5
print("After changing the first element:", numbers)
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

numbers.sort(reverse=True)
print("Sorted descending:", numbers)

numbers.reverse()
print("Reversed:", numbers)

copied_numbers = numbers.copy()
copied_numbers.append(999)
print("Original after modifying its copy:", numbers)
print("Modified copy:", copied_numbers)

squares = [number ** 2 for number in numbers]
print("Squares:", squares)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
