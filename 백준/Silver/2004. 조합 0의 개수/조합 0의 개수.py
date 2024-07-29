def cnt_factors_of_five(num, i):
    cnt = 0
    while num >= i:
        cnt += num // i
        num = num // i
    return cnt

m, n = map(int, input().split())

cnt1 = cnt_factors_of_five(m, 5) - cnt_factors_of_five(m-n, 5) - cnt_factors_of_five(n, 5)
cnt2 = cnt_factors_of_five(m, 2) - cnt_factors_of_five(m-n, 2) - cnt_factors_of_five(n, 2)

print(min(cnt1, cnt2))

# 주어진 수 num이 있을 때,
# num!이 몇 개의 0으로 끝나는지, 
# 즉 num!에서 5의 개수를 구하는 법(2는 짝수 때문에 차고 넘친다)은
# num//5 != 0인 동안 무한 반복하여 더해주면 된다.

# 예를 들어 num = 24인 경우
# 24 // 5 = 4
# 4 // 5 = 0이므로
# cnt = 4이다. 
# 이는 한편으로, 5의 배수를 4번 지나쳐왔음을 의미한다.
# 즉 5, 10, 15, 20 -> 5, 5*2, 5*3, 5*4을 지나쳐왔으므로 5가 4번 존재한다.

# num = 26인 경우
# 26 // 5 = 5
# 5 // 5 = 1
# 1 // 5 = 0이므로
# cnt = 6이다.
# 이는 위와 동일선상에서 5를 5번 거쳐왔음을 의미함과 동시에 5의 제곱을
# 인수로 가지는 수가 존재함을 의미한다.
# 즉 5, 10, 15, 20, 25 -> 5, 5*2, 5*3, 5*2*2, 5*5를 지나쳐왔으므로
# 5가 6번 존재한다.