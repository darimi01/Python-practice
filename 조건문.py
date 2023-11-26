#두 수 비교하기
a,b=map(int,input().split())

if a<b:
    print("<")
elif a>b:
    print(">")
else:
    print("==")
    
#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a=int(input())

if 90<=a<=100:
    print("A")
elif 80<=a<90:
    print("B")
elif 70<=a<80:
    print("C")
elif 60<=a<70:
    print ("D")
else:
    print("F")
    
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
#윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
#예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
a=int(input())

if a%4==0:
    if a%100!=0:
        print(1)
    elif a%400==0:
        print(1)
    else:
        print(0)
else:
    print(0)

#하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것
x=int(input())
y=int(input())

if 0<x:
    if 0<y:
        print(1)
    else:
        print(4)
else:
    if 0<y:
        print(2)
    else:
        print(3)

#오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산
a,b=map(int,input().split())
c=int(input())

d=a*60+b+c

print("{} {}".format((d//60),(d%60)))

#주사위 세개
a,b,c=map(int,input().split())

if a==b==c:
    print("{}".format(10000+(a*1000)))
elif a==b:
    print("{}".format(1000+(a*100)))
elif c==b:
    print("{}".format(1000+(b*100)))
elif a==c:
    print("{}".format(1000+(a*100)))
else:
    if a>b and a>c:
        print(a*100)
    elif b>c and b>a:
        print(b*100)
    elif c>b and c>a:
        print(c*100)





