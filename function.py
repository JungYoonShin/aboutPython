#예제1)
def printHello():
    print("Hello, user")

printHello()

#예제2)
def  printHi(name):
    print("Hi, ", name)

name = input("당신의 이름은? ")
printHi(name)

#예제3)
def printWelcome(user):
    word = "Welcome, " + str(user)
    return word

user = input("당신의 이름은? ")
print(printWelcome(user))

#예제4)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c = func_mul(10)
print(a,b,c)
#list = func_mul(10)
#print(list)

#1 문자열 안에 원하는 값 삽입 -> 문자열 formatting
print("저는 덕성 멋사 {}기 입니다.".format(9))

fruit = input("당신이 좋아하는 과일은? ")
print("내가 좋아하는 과일은 {}입니다.".format(fruit))

#숫자는 인덱스, 문자는 이름으로 대입
print("저는 {0}학번 {major}과입니다.".format(18, major="컴퓨터 공학")) 