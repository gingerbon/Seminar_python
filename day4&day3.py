# 최대공약수와 최소공배수
def solution(n, m):
    def minn(a,b): # 최소공배수 찾기
        # a<b swap 만들어주기
        if (a > b):
            a,b = b,a # swap 조심!
            
        if b%a == 0:
            return a # 최대공약수
        else:
            return minn(a, b%a) # 유클리드 호제법 ?  
        
    c = minn(n, m) # 최대공약수 c
    d = n*m/c #최소공배수 d
    e = [c,d]
    return e
# 최대공약수와 최소공배수 recursion 안쓴거
    def solution(n, m):
    answer = []
    # 12랑 18의 경우 최소공배수 36 최대공약수 6
    # n의 약수 목록
    a = []
    for i in range(1, n+1):
        if n%i == 0:
            a.append(i)
    # m의 약수 목록
    b = []
    for j in range(1, m+1):
        if m%j == 0:
            b.append(j)  
    # 공통약수
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(b[j])
    # 최대공약수
    d = c[len(c)-1]
    # 최소공배수
    e = n*m/d
    f = [d,e]
    return f
# x만큼 간격이 있는 n개의 숫자
    def solution(x, n):
      answer = []
      for i in range(n):
        num = x + x*i
        answer.append(num)
      return answer
