# 풀이 시간 - 30분
# 정답

location = input()

x = int(location[1])
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = alphabet.index(location[0])+1

step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for i in step:
    nx = x + i[0]
    ny = y + i[1]
    if (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
      count += 1  

print(count)