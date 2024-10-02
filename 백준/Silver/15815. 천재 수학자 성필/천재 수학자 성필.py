if __name__ == '__main__':

    expression = input()
    stack = []

    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        else:
            if stack:
                n2 = stack.pop()
                n1 = stack.pop() 
                # stack이므로 들어간 순서와 나왔을 때 순서가 달라짐.
                # 즉 수식의 내용이 달라질 수 있으니 바꿔줘야 함.
                if i == '*':
                    stack.append(n1 * n2)
                elif i == '/':
                    stack.append(n1 // n2) # 연산 결과가 정수만 나올 수 있으므로 몫 연산자 사용
                elif i == '+':
                    stack.append(n1 + n2)
                elif i == '-':
                    stack.append(n1 - n2)

    print(stack[-1])