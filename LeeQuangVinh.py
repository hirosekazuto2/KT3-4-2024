""" đề bài(python)
- đọc 1 file văn bản gồm nhiều dòng
-ghi ra màn hình thoe thứ tự ngược lại của các dòng """

with open('kiemtra.txt', 'r') as file:
    lines = file.readlines()
    lines.reverse()
    for line in lines:
        print(line.strip()) 

