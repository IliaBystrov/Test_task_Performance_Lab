file_path = input("Укажите путь к файлу: ")

with open(file_path, 'r') as f:
    nums = []
    for line in f:
        nums.append(int(line))

avg = sum(nums)//len(nums)
count=0

for i in range (len(nums)):
    while nums[i]!=avg:
        if nums[i]<avg:
            nums[i]+=1
            count+=1
        else:
            nums[i]-=1
            count+=1

print(count)