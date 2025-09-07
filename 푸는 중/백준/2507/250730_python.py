# 파이썬은 datetime 이라는 모듈을 임포트해야 날짜를 뽑을 수 있음

# 원하는 형식으로 출력하려면 strftime() 메서드를 사용

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))


# 맞춘 문제 자동화
# import requests

# boj_id = 'your_boj_id'  # 자신의 백준 아이디로 바꿔야 함
# url = f"https://solved.ac/api/v3/user/show?handle={boj_id}"

# data = requests.get(url).json()
# print(data['solvedCount'])  # 맞은 문제 개수
# print(data['handle'])       # 아이디

'''
print("\\    /\\")
print(' )  ( \')')
print("(  /  )")
print(" \(__)|")

print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")
'''

'''a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)'''

numbers = list(map(int, input().split()))
print(sum(numbers))