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


#10 문자열에서 하나의 문자 뽑아내기
# 자료형 - 문자열과 배열 인덱싱 ( 0, -1 ) 

makit='Sieun Woojin!'
result = makit[0]
print(result)

result = makit[6]
print(result)

result = makit[-1]
print(result)

#11 문자열에서 여러 문자 뽑아내기
# 문자열 슬라이싱 [ : : ] 

makit = 'Sieun Woojin!'
result = makit[2:9]
print(result)
result = makit[0:5]
print(result)
result = makit[6:]
print(result)

#12 동쪽을 찾아라
makit = '동서남북동서남북동서남북'
print(makit[ ::4])
