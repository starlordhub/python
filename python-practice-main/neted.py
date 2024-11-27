print('main started')
try:
    print('outer try is stared')
    print('a')
    try:
        print('inner try is started')
        print(10/2)
        print('inner try is ended')
    except Exception as e:
        print(e)
    print('outer is end')
except Exception as e:
    print(e)
print('main ended')
