t1 = "abefg"
t2 = "abcde"

answer = [[ 0 for i in range( 5 )] for i in range( 5 )]

i = 0
while i < 5:
    j = 0
    num = 0
    while j < 5:
        if t1[ i ] == t2[ j ]:

            i_ = i
            while i_ < 5 :
                j_ = j
                while j_ < 5:
                    answer[ i_ ][ j_ ] += 1
                    j_ += 1
                i_ += 1

        j += 1
    i+= 1

for i in answer:
    print(i)
print("가장 긴 공통의 부분문자열 : ", answer[4][4])

