
def ant( object , count ):
    if count == 0:
        return
    else:
        next = zip( object , "" , [0 ,"",0] )
        return ant( next , count - 1)

def zip( object , result , data ):   # data[ 확인중인index , 연속으로 등장중인 문자 , 연속된 횟수 ]
    if data[0] == len(object):
        if data[2] > 0 :
            result += str( data[2] )
        print( result )
        return result
    else:
        if object[data[0]] != data[1]:
            if data[2] > 0 :
                result += str( data[2] )
            data[1] = object[data[0]]
            result += data[1]
            data[2] = 1
        else:
            data[2] += 1
        data[0] += 1
        return zip( object , result , data )

print("1")
ant("1",20)
