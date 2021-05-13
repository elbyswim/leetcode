def sumFourDivisors(nums):
    answer = 0
    for num in nums:
        divisors = []
        i = 1
        while i ** 2 <= num:
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
            i += 1
        if len(divisors) == 4:
            answer += sum(divisors)
    return answer

print(sumFourDivisors([21, 4, 7]))
