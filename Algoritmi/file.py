# p(non-a) = 365/365 * 364/365 * 363/365 * ... * (343)/365 = (1/365**(23)) 365*...*343
# p(a) = 1 - p(non-a)


prod = 1
for i in range(343, 366):
    prod *= i/365

print(1-prod)