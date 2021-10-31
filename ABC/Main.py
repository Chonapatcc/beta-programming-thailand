num=input().split()
nums=[]
for anum in num:
    nums.append(int(anum))
lis=input()
st=[]

for i in range(3):
    if lis[i]=="A":
        st.append(1)
    elif lis[i]=="B":
        st.append(2)
    else:
        st.append(3)

if st[0]>st[-1]:
    if nums[0]>nums[-1]:
        pass
    else:
        a,b=nums[0],nums[-1]
        nums[0]=b
        nums[-1]=a
else:
    if nums[0]>nums[-1]:
        a,b=nums[0],nums[-1]
        nums[0]=b
        nums[-1]=a
    else:
        pass
for i in range(1,3):
    if st[i-1]<st[i]:
        if nums[i-1]>nums[i]:
            a,b=nums[i-1],nums[i]
            nums[i-1]=b
            nums[i]=a
        else:
            pass
    else:
        if nums[i-1]>nums[i]:
            pass
        else:
            a,b=nums[i-1],nums[i]
            nums[i-1]=b
            nums[i]=a


word=""
for num in nums:
    word+=str(num)+" "
print(word.rstrip())