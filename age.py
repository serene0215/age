driving = input('請問你有開過車嗎:')
if driving != '有' and driving != '沒有':
    print('只能輸入有或沒有')
    raise SystemExit
age = input('請問你的年齡：')
if driving == '有':
    if int(age) >= 18:
        print('你有合法')
    else:
        print('未成年不行開車')
elif driving == '沒有'
    if int(age) >= 18:
        print('你可以考駕照了')
    else:
        print('你快要可以考駕照了')            