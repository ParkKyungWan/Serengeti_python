object = "1"
for i in range( int(input()) ):
    print( object )
    line = ""
    now = ""
    count = 0
    for char in object:
        if now != char:
            if count >=1:
                line += str(count)
            now = char
            line += char
            count = 1
        else:
            count += 1
    line += str(count)
    object = line


