# [Silver II] 조합 0의 개수 - 2004 

[문제 링크](https://www.acmicpc.net/problem/2004) 

----

```
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


# 그래도 안되서 재확인
# 팩토리얼은 5의 개수만 세도 문제가 생기지 않지만
# 조합은 팩토리얼을 팩토리얼로 나눈 식이므로
# nCr = 15 = 3 * 5와 같이
# 2의 개수 < 5의 개수인 경우가 발생할 수 있다고 한다.
# 따라서 2의 개수와 5의 개수를 모두 센 다음
# 더 작은 값을 반환해야 함.
```

----

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

수학, 정수론

### 제출 일자

2024년 7월 29일 17:12:44

### 문제 설명

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c28 TEX-S1"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac atop="true" delims="true" style="vertical-align: -0.345em;"><mjx-num style="padding-bottom: 0.469em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-den><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c29 TEX-S1"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="1.2em" maxsize="1.2em">(</mo></mrow><mfrac linethickness="0"><mi>n</mi><mi>m</mi></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="1.2em" maxsize="1.2em">)</mo></mrow></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \choose m$</span></mjx-container>의 끝자리 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>의 개수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>m</mi><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le m \le n \le 2,000,000,000$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2260"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>≠</mo><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \ne 0$</span></mjx-container>)이 들어온다.</p>

### 출력 

 <p>첫째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c28 TEX-S1"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac atop="true" delims="true" style="vertical-align: -0.345em;"><mjx-num style="padding-bottom: 0.469em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-den><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c29 TEX-S1"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="1.2em" maxsize="1.2em">(</mo></mrow><mfrac linethickness="0"><mi>n</mi><mi>m</mi></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="1.2em" maxsize="1.2em">)</mo></mrow></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \choose m$</span></mjx-container>의 끝자리 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>의 개수를 출력한다.</p>

