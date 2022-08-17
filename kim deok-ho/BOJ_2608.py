# 로마숫자
romaNum1 = list(input())
romaNum2 = list(input())

# 로마 숫자 변환
def rtoa(romaNum):
    # 로마 숫자 길이
    numLen = len(romaNum)
    # 아라비안 숫자
    arab = 0
    # 인덱스
    idx = 0
    # 인덱스가 로마 숫자 길이 -1까지 반복
    while idx < numLen:
        # C가 오는 경우
        if romaNum[idx] == 'C':
            if idx != numLen -1:
                # 다음에 M이 오면
                if romaNum[idx+1] == 'M':
                    # 900
                    arab += 900
                    # M 다음부터 확인
                    idx += 2
                # 다음에 D가 오면
                elif romaNum[idx+1] == 'D':
                    # 400
                    arab += 400
                    # D 다음부터 확인
                    idx += 2
                # 그 외
                else:
                    # 100
                    arab += 100
                    idx += 1
            else:
                # 100
                arab += 100
                idx += 1
        # M이 오는 경우
        elif romaNum[idx] == 'M':
            # 1000
            arab += 1000
            idx += 1
        # D가 오는 경우
        elif romaNum[idx] == 'D':
            # 500
            arab += 500
            idx += 1
        # X가 오는 경우
        elif romaNum[idx] == 'X':
            if idx != numLen - 1:
                # 다음에 C이 오면
                if romaNum[idx + 1] == 'C':
                    # 90
                    arab += 90
                    # C 다음부터 확인
                    idx += 2
                # 다음에 L가 오면
                elif romaNum[idx + 1] == 'L':
                    # 40
                    arab += 40
                    # L 다음부터 확인
                    idx += 2
                # 그 외
                else:
                    # 10
                    arab += 10
                    idx += 1
            else:
                # 10
                arab += 10
                idx += 1
        # L이 오는 경우
        elif romaNum[idx] == 'L':
            # 50
            arab += 50
            idx += 1
        # I가 오는 경우
        elif romaNum[idx] == 'I':
            if idx != numLen - 1:
                # 다음에 X가 오면
                if romaNum[idx + 1] == 'X':
                    # 9
                    arab += 9
                    # X 다음부터 확인
                    idx += 2
                # 다음에 V가 오면
                elif romaNum[idx + 1] == 'V':
                    # 4
                    arab += 4
                    # V 다음부터 확인
                    idx += 2
                # 그 외
                else:
                    # 1
                    arab += 1
                    idx += 1
            else:
                # 1
                arab += 1
                idx += 1
        # V가 오는 경우
        elif romaNum[idx] == 'V':
            # 5
            arab += 5
            idx += 1
    return arab
arabNum = rtoa(romaNum1) + rtoa(romaNum2)
print(arabNum)

# 아라비아 숫자 변환
def ator(arabNum):
    # 로마 숫자
    romaNum = ''
    # 0보다 크면 반복
    while arabNum:
        # 1000으로 나눌 수 있으면
        if arabNum // 1000:
            # 값만큼 M을 추가
            romaNum += 'M'*(arabNum // 1000)
            # 아라비안 숫자 업데이트
            arabNum = arabNum % 1000
        # 900으로 나눌 수 있으면
        elif arabNum // 900:
            # CM 추가
            romaNum += 'CM'
            # 업데이트
            arabNum = arabNum % 900
        # 500으로 나눌 수 있으면
        elif arabNum // 500:
            # D 추가
            romaNum += 'D'
            arabNum = arabNum % 500
        # 400
        elif arabNum // 400:
            romaNum += 'CD'
            arabNum = arabNum % 400
        # 100
        elif arabNum // 100:
            # 값만큼 C 추가
            romaNum += 'C'*(arabNum // 100)
            arabNum = arabNum % 100
        # 90
        elif arabNum // 90:
            romaNum += 'XC'
            arabNum = arabNum % 90
        # 50
        elif arabNum // 50:
            romaNum += 'L'
            arabNum = arabNum % 50
        # 40
        elif arabNum // 40:
            romaNum += 'XL'
            arabNum = arabNum % 40
        # 10
        elif arabNum // 10:
            # 값만큼 추가
            romaNum += 'X'*(arabNum // 10)
            arabNum = arabNum % 10
        # 9
        elif arabNum // 9:
            romaNum += 'IX'
            arabNum = arabNum % 9
        # 5
        elif arabNum // 5:
            romaNum += 'V'
            arabNum = arabNum % 5
        # 4
        elif arabNum // 4:
            romaNum += 'IV'
            arabNum = arabNum % 4
        # 1
        else:
            # 값만큼 I 추가
            romaNum += 'I'*(arabNum // 1)
            arabNum = arabNum % 1
    return romaNum
print(ator(arabNum))
