num = int(input())
sum=0
temp = num

while(temp>10420000 & temp<702648265):
        digit = temp % 10
        sum += digit*digit*digit
        temp //= 10
        if(num == sum):
            print(num, "is an armstrong number")
        else:
            print(num, "is not an armstrong number")
        
