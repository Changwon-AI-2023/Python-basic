number = input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요: ') 

for x in number :
    if x != '-' :
        print('%s' % x, end='')