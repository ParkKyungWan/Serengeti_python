
def ant( object , count ):
    if count == 0:
        return
    else:
        next = zip( object , "" , data())
        return ant( next , count - 1)

def zip( object , result , data ):
    if data.index == len(object):
        if data.count > 0 :
            result += str( data.count )
        print( result )
        return result
    else:
        if object[data.index] != data.char:
            if data.count > 0 :
                result += str( data.count )
            data.char = object[data.index]
            result += data.char
            data.count = 1
        else:
            data.count += 1
        data.index += 1
        return zip( object , result , data )

class data:
    index = 0  # 문자열 object 에서 index 번째 char 확인중
    char = ""  # char 이 연속으로 발견되는 중
    count = 0  # 지금까지 char 은 count 번 등장

print("1")
ant("1",20) #20번
