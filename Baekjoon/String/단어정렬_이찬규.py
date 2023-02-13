# 정답

[print(word) for word in sorted(list(set([input() for _ in range(int(input()))])), key=lambda x: (len(x), x))]
