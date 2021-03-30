def solution(phone_book):
    answer = True
    i = 0
    phone_book = sorted(phone_book)
    for j in range(i+1, len(phone_book)):
        cmp1 = phone_book[i]
        cmp2 = phone_book[j]
        if cmp2.startswith(cmp1):
            answer = False
            break
        i += 1
    return answer