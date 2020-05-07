file_name = input("파일의 이름을 입력해주세요 : ")
option = int(input("1 : 압축 , 2 : 압축해제 \n-> "))
if option==1:
    file = open("./"+file_name,'r')
    text = file.read()

    text_zip = ""
    now = ""
    count = 0

    for char in text:
        if now != char:
            if count >=1:
                text_zip += "(" + str(count) + ")"
            now = char
            text_zip += char
            count = 1
        else:
            count += 1
    text_zip += "(" + str(count) + ")"

    print("압축 결과 : ", text_zip)
    file.close()

    file = open("./"+file_name,'w')
    file.write(text_zip)
    file.close()

else:

    file = open("./" + file_name, 'r')
    text_zip = file.read()

    Repetition = False
    repeat_char = ""
    how_much_repeat = ""

    text = ""

    for c in text_zip:
        if c == "(":
            Repetition = True
        elif c == ")":
            for i in range(int(how_much_repeat)):
                text += repeat_char
            Repetition = False
            how_much_repeat = ""
        else:
            if Repetition:
                how_much_repeat += c
            else:
                repeat_char = c

    print("압축해제 결과 : ", text)
    file.close()

    file = open("./" + file_name, 'w')
    file.write(text)
    file.close()





