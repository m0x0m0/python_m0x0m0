k, m, n = map(int, input().split())
res = m * (2 * (n // k) + (n % k != 0) + ((n % k > k / 2.0) or (n < k)))
print(res)