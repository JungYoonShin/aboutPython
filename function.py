#����1)
def printHello():
    print("Hello, user")

printHello()

#����2)
def  printHi(name):
    print("Hi, ", name)

name = input("����� �̸���? ")
printHi(name)

#����3)
def printWelcome(user):
    word = "Welcome, " + str(user)
    return word

user = input("����� �̸���? ")
print(printWelcome(user))

#����4)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c = func_mul(10)
print(a,b,c)
#list = func_mul(10)
#print(list)

#1 ���ڿ� �ȿ� ���ϴ� �� ���� -> ���ڿ� formatting
print("���� ���� �ڻ� {}�� �Դϴ�.".format(9))

fruit = input("����� �����ϴ� ������? ")
print("���� �����ϴ� ������ {}�Դϴ�.".format(fruit))

#���ڴ� �ε���, ���ڴ� �̸����� ����
print("���� {0}�й� {major}���Դϴ�.".format(18, major="��ǻ�� ����")) 