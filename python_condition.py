# number = int(input())

# if number < 5:
#     print("숫자가 5보다 작습니다.")
# elif 5 < number < 10:
#     print("5보다 크고 10보다 작다")
# else:
#     print('10보다 큽니다.')

# money = int(input())

# if money == 70000:
#     print('비행기')
# elif money == 50000:
#     print('기차')
# elif money == 30000:
#     print('버스')
# else:
#     print('걸어간다')

# for i in range(10):
#     print('Hello world')

# countries = ['kor','usa','china']
# for country in countries:
#     print(country)

# for country in 'countries':
#     print(country)

countries = ['kor','usa','china']
for country in countries:
    if country == 'kor':
        print('한글로 분석해주세요.')
    elif country == 'usa':
        print('영어로 분석해주세요.')
    elif country == 'china':
        print('중국어로 분석해주세요.')
