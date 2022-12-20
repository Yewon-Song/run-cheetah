##2.1.3 연습문제: 얌체공
## round()는 반올림을 해주는 함수임
## round(2.675, 2)를 하면 2.67로 나오는데 이는 부동소수점 연산의 한계임
## while문은 ~~~조건이라면 계속 시행하는 것임!!!
number=358
rem=rev=0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem 
    number = number // 10
print(rev)