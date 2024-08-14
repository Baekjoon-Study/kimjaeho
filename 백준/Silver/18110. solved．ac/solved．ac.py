import sys

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    if not n:
        print(0)
        exit()
    outlier = my_round(n * 0.3 * 0.5)
    # print(outlier)

    reviews = []
    for _ in range(n):
        reviews.append(int(sys.stdin.readline()))
    reviews.sort()

    reviews = reviews[outlier:-outlier] if outlier else reviews
    # print(reviews)

    result = my_round(sum(reviews)/len(reviews))
    print(result)