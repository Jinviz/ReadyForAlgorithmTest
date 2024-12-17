a,b = sorted(map(int, input().split()))

# 최대공약수 (유클리드 호제법)
def GCD(a,b):
  while b != 0:
    a, b = b, a%b
  return a

# 최대공배수 (두 수의 곱/최대공약수)
def LCM(a,b):
  return (a * b)//GCD(a,b)

print(GCD(a,b))
print(LCM(a,b))