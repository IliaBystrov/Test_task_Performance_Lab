import sys

if len(sys.argv) == 2:
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        nums = []
        for line in f:
            nums.append(int(line))

    avg = sorted(nums)[len(nums) // 2]
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
else:
    print("Не указан путь к файлу!")