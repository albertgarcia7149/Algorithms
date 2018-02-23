def fib(n):
	print(Memo)
	if n==1 or n==2:
		return Memo[1]
	elif Memo[n-1] != -1:
		return Memo[n-1]
	else:
		Memo[n-1]=(fib(n-1)+fib(n-2))
		return Memo[n-1]

num=int(raw_input("Enter A Fib Number:"))
Memo=[-1]*num
Memo[0]=1
Memo[1]=1
print(fib(num))