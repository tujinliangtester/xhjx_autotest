from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn, s1) + reduce(fn, s2) / (10 ** len(s2))  # 乘幂

if __name__=='__main__':
    print(1111)
    print(str2float('0.05'))