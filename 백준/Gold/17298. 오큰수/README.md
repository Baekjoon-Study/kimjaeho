# [Gold IV] 오큰수 - 17298 

----
계속 시간 초과 나오길래 열받아서 GPT한테 물어봤다.<br>
그랬더니 스택을 활용해서 문제를 해결하는 걸 보여줌....<br>
내가 짠 코드는 모든 인덱스에 걸쳐 더 큰 수가 나올 때까지 탐색을 해야하므로 시간복잡도가 $O(n^2)$인데, 시간을 줄이기 위해서는 스택을 이용하여 한 번만 탐색하도록 해야 한다는 것.<br>
<br>
```python title:'내 코드'
import sys

n = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
result = [-1] * n

for i in range(n):
    idx = i+1
    while idx < len(nge):
        if nge[i] < nge[idx]:
            result[i] = nge[idx]
            break
        idx += 1
    
print(' '.join(map(str, result)))
```
<br>
아래는 chat GPT가 짠 코드<br>
```python title:'GPT 코드'
import sys

n = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
result = [-1] * n

stack = []

for i in range(n):
    while stack and nge[stack[0]] < nge[i]:
        result[stack.pop(0)] = nge[i]
    stack.append(i)

print(' '.join(map(str, result)))
```

9 5 4 8 과 같은 일련의 숫자가 입력되는 경우<br>
내가 짠 코드에서는<br>
9 $\rightarrow$ 5, 4, 8<br>
5 $\rightarrow$ 4, 8<br>
4 $\rightarrow$ 8<br>
이렇게 인덱스마다 탐색해야 한다.<br>
<br>
GPT가 짠 코드의 로직은 아래와 같다.<br>
9, 5, 4에 이르기까지는 변화가 없다. 대신 이때 각 인덱스를 stack에 push한다.<br>
이후 i=3에서 4<8이므로 4에 해당하는 index를 pop하여 4 위치에 8을 대입한다.<br>
같은 방식으로 5<8도 똑같이 대입하며, 9의 경우 9>8이므로 pass한다.<br>
이러면 최종적으로 [-1, 8, 8, -1]의 결과가 나오게 된다.<br>
<br>
근데 큐는 왜 쓰면 안되는 걸까?<br>
괜히 호승심이 생겨 한 번 해봤는데 queue의 첫번째 항목이 9이므로 9>8이다. 따라서 더 진행되지 않는다.<br>
즉 스택에 수가 쌓이는 이유는 이전 인덱스보다 다음 인덱스의 수가 작기 때문이므로 스택을 사용하여 더 작은 수부터 큰 수까지 차례대로 대체하는 것.<br>
<br>
그냥 쓰기 그래서 뭐라도 내 방식으로 바꿔보려 했지만 너무 간결해서 손댈 부분이 없다.

----

[문제 링크](https://www.acmicpc.net/problem/17298) 

### 성능 요약

메모리: 202408 KB, 시간: 960 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 7월 5일 22:22:44

### 문제 설명

<p>크기가 N인 수열 A = A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 있다. 수열의 각 원소 A<sub>i</sub>에 대해서 오큰수 NGE(i)를 구하려고 한다. A<sub>i</sub>의 오큰수는 오른쪽에 있으면서 A<sub>i</sub>보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.</p>

<p>예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.</p>

### 입력 

 <p>첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub> (1 ≤ A<sub>i</sub> ≤ 1,000,000)이 주어진다.</p>

### 출력 

 <p>총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.</p>

