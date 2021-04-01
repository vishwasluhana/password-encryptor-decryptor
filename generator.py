import random
def file_writing(hash,file,function):
    while len(hash) < 5:
        hash = hash + random.choice(random.choice(all))
    if function == "mid_line":
        file.write(f'"{hash}",')

    elif function == "line_end":
        file.write(f'"{hash}"],\n')

    else:
        file.write(f'"{hash}"]{"}"}')

short = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' '))
long = list("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' '))
numbers = list("1 2 3 4 5 6 7 8 9 0".split(' '))
char = list("! @ # $ ^ & * ( ) _ - = + [ ] | : ; , . / ? ~".split(' '))
all = [short, long, numbers, char]
# File is opened in append mode
file = open('result.py','a')
file.write("hash_data = {")
for list in all:
	# Sublist means each character in short, long, numbers and char
    for sublist in list:
        file.write(f'"{sublist}":[')
        for i in range(5):
            hash = ""
            if list == all[-1] and sublist == list[-1]:
                if i == 4:
                    file_writing(hash,file,"result_end")
                else:
                    file_writing(hash,file,"mid_line")
            elif i == 4:
                file_writing(hash,file,"line_end")
            else:
                file_writing(hash,file,"mid_line")
