#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

i = 2
count = 2 # Counting 2 and 3
prime = false
loop do
	j = 2
	loop do 
		if j>i/2 
			break 
		end
		# If i has any factors it is not prime
		if i%j==0
			prime = false
			break
		end
		prime = true
		j+=1
	end
	if prime
		count+=1
	end
	
	if count == 10001
		p i
		break
	end
	i+=1	
	
end	