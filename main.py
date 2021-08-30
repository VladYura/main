#Найти объём между наибольшими числами
#height = [1, 2, 1]
#
#a = 0
#b = len(height) - 1
#sum = 0
#while a < b:
#    sum = max(sum, min(height[a], height[b]) * (b - a))
#    if height[a] < height[b]:
#        a += 1
#    else:
#        b -= 1
#print(sum)

#Преобразовать обычные цифры в римские

num = 1941
nums = str(num)
out = []
tran = {1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"}

l = len(nums)

for i in nums:
    if l == 4:
        for j in range(int(i)):
            out.append(tran[1000])
    elif l == 3:
        if