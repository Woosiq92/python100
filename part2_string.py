#7 한줄 띄기 

# 여러가지 풀이 
a = '시은 우진'
a = a + "화이팅!!'
print(a)
print() 
print(a)

#8 입력받아 컴퓨터랑 대화하기 

# 문자열과 숫자형 연산 

a = input('이름이 무엇인가요? ')
b = int(input('몇 살인가요? ')) 
print(a, '님은 내년에는', b+1 ,'살이 됩니다.')

# 9 두 수를 입력받아 합과 평균 구하기

# 개념 : 자료형 ( int, float ) , 평균 연산을 위한 괄호 

a = int(input()) 
b = float(input())

print("a와 b의 합은", a+b) 
print("a와 b의 평균값은", (a+b)/2)
