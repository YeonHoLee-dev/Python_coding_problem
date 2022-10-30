# -로 나눌 경우
# 10 - 20 + 30 - 40 -> 10, 20 + 30, 40
# 10 - 20 + 30 - 40 + 50 - 60 -> 10, 20+30, 40+50, 60
# 이후 구분된 각각의 문자열에서 +로 구분한다.
# 첫번째 리스트에서 나머지 리스트의 숫자의 합(_sum)을 뺀 값을 반환한다.

a = input().split('-')
f = sum(list(map(int, a[0].split('+'))))

for x in a[1:]:
    f -= sum(list(map(int, x.split('+'))))

print(f)
