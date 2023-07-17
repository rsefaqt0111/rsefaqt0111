#프로그램<-입력과 출력을 생각하자

#x = input("x의 값을 입력하세요: ")
#def gugu(n):
#    result = []
#    for m in range(1,10):
#        result.append(int(n)*int(m))
#    return result
#print(gugu(x))

def gugu(n):
    result = []
    for m in range(1,10):
        result.append(int(n)*m)
    return result
print(gugu(input("x의 값을 입력하세요:")))
