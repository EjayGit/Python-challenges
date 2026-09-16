# Print all pronic numbers between 1 and 100. P𝑛 = num = 𝑛 ∗ (𝑛 + 1) = 𝑛^2 + 𝑛

lower = 1
upper = 100

def isPronic(num):
    # where 𝑛 < sqrt(P𝑛)
    for n in range(1, int(num**0.5)+1):
        if (n * (n+1)) == num:
            return True

for num in range(lower, upper):
    if isPronic(num):
        print(num)