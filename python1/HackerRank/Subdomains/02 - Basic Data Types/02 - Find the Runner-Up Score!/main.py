if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    first = max(scores)
    runner_up = max([s for s in scores if s != first])
    print(runner_up)