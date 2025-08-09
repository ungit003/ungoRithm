def finder(list, number, l_index, r_index):
    if l_index > r_index:
        return 0
    center_index = (l_index + r_index) // 2
    center_number = list[center_index]
    if center_number == number:
        return 1
    elif center_number > number:
        return finder(list, number, l_index, center_index - 1)
    elif center_number < number:
        return finder(list, number, center_index + 1, r_index)

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
findings = list(map(int, input().split()))

nums.sort()
for finding in findings:
    if nums[-1] < finding or nums[0] > finding:
        print(0)
        continue
    print(finder(nums, finding, 0, N - 1))