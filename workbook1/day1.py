# 12865
n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input().split())
    arr[i][0] = int(arr[i][0])
    arr[i][1] = int(arr[i][1])

# 가장 큰 값
max_v = 0

# select개 선택하는 경우
for select in range(1, n+1):

    # select개의 각각의 인덱스
    idx = []
    for i in range(select):
        idx.append(i)

    # select개 선택하는 각각의 경우 검사
    while(1):
        # 무게 합과 가치 합
        all_w = 0
        all_v = 0
        for i in idx:
            all_w += arr[i][0]
            all_v += arr[i][1]
        if (all_w <= k and all_v > max_v):
            max_v = all_v

        #첫번째 인댁스가 꽉 차면 종료
        if (idx[0] >= n - select):
            break

        # 마지막 포인터의 인덱스가 끝나는지 검사, i: 마지막 인덱스
        for i in range(select-1, -1, -1):
            if (idx[i] <= n - (select - i)-1):
                idx[i] += 1
                # 다음 인덱스 세팅
                for j in range(i+1, select):
                    idx[j] = idx[j-1] + 1
                break
            # 만약 꽉 차면 아래 인덱스 추가
print(max_v)