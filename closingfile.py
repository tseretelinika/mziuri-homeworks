# #1
# with open("workfile", "w") as f:
#     f.write("gg")
#
# #2
# with open("workfile", "r") as g:
#     for line in g:
#         print(len(line))
#
#
# #3
# with open("workfile", "a") as s:
#     s.write("\n" + "baro dzma")
#
# #4
# with open("workfile", "r", encoding="UTF-8") as f:
#     b = f.read()
# with open("gg", "w", encoding="utf-8") as a:
#     a.write(b)

#5
# a = open("aa", "r")
# b = open("workfile", "r")
# c = open("file2", "w")
# for j in a:
#     c.write(j)
#     for d in b:
#         c.write(d)

#6
# file = open("workfile", "r+")
# file1 = file.read()
# file1 = file1.upper()
# file.write(file1)
# print(file1)

#7
while True:
    a = input("shemoiyvane info")
    if a == "0":
        print("vso")
    else:
        with open("data.txt", "w") as g:
            g.write(a + "\n")