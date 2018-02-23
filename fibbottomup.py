num=int(raw_input("Enter A Fib Number:"))
out=0
Memo=[-1]*num
Memo[0]=1
Memo[1]=1
for i in range(3,num+1):
	Memo[i-1]=Memo[i-2]+Memo[i-3]

print(Memo[num-1])