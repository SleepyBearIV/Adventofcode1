
#splits the teixt in to array
with open('input_1A.txt', 'r') as file:
    inputArray = file.read().split("\n")


inputNumbers = []
def extract_nums(string):
    nums = []

    for char in string:
        if char.isdigit():
            if len(nums) > 1:
                nums.pop()
                num = int(char)
                nums.append(num)
            else:
                num = int(char)
                nums.append(num)
                nums.append(num)
    number = int("".join(str(i) for i in nums))
    return number

for x in inputArray:
    extract_nums(x)
    inputNumbers.append(extract_nums(x))

sum = 0

for i in inputNumbers:
    sum = sum + i
print(sum)
