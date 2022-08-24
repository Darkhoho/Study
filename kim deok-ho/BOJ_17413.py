S = input()

ans = ''
word = ''
i = 0
while i < len(S):
    if S[i] == '<':         # 태그 시작
        word += S[i]
        while S[i] != '>':  # 태그 종료
            i += 1
            word += S[i]
        ans += word         # 단어 추가
        word = ''           # 단어 초기화

    elif S[i] != ' ':       # 특수 문자, 공백 이외에 전부 거꾸로 입력
        word = S[i] + word
        
    else:                   # 공백인 경우 저장된 단어 리스트 추가
        ans += word + ' '
        word = ''           # 단어 초기화
    i += 1

if word:                    # 단어가 남았으면 리스트에 추가
    ans += word
print(ans)