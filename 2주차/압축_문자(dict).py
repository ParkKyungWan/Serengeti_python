file_name = input("파일의 이름을 입력해주세요 : ")
option = int(input("1 : 압축 , 2 : 압축해제 \n-> "))
if option==1:
    file = open("./"+file_name, 'r')
    text = file.read()

    words = {}

    나머지 = ""
    if len(text)%2 !=0:
        나머지 = text[len(text) - 1]
        words[나머지] = 나머지
        text = text[ : len( text ) - 1]


    i = 0
    ascii = 65
    while i < len( text ):
        now = text[ i ] + text[ i+1 ]
        if not now in words:
            words[ now ] = chr( ascii )
            ascii += 1
        i += 2

    file.close

    text_zip = ""
    i = 0
    while i < len( text ):
        now = text[ i ] + text[ i+1 ]
        text_zip += words[ now ]
        i += 2

    file = open("./" + file_name, 'w')
    dict_str = str( words )
    file.write(text_zip + 나머지 + " //" + dict_str)
    print("결과: ", text_zip + 나머지)
    file.close()

if option == 2:
    file = open("./" + file_name, 'r')
    text = file.read()

    i = 0
    words = {}

    while i < len( text ) - 1 :
        if text[ i ] + text [ i + 1 ] == "//":
            dict_str = text[ i+2 : ]
            words = eval( dict_str )
            text = text[ : i ]; break;
        i += 1
    for (k, v) in words.items():
        text = text.replace( v, k, text.count(v) )
    file.close

    file = open("./" + file_name, 'w')
    file.write(text)
    print("결과: ", text)
    file.close()



