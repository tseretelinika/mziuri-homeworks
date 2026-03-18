procent_f = 0
procent_m = 0
sur_f = 0
dead_f = 0
sur_m = 0
dead_m = 0
st_class = 0
nd_class = 0
rd_class = 0
all_class = 0
with open("titanic.txt", "r") as f:
    f.readline()
    for line in f:
        data = line.strip().split(",")
        if data[4] == "female":
            procent_f += 1
        elif data[4] == "male":
            procent_m += 1

        if data[1] == "1" and data[4] == "female":
            sur_f += 1
        elif data[1] == "0" and data[4] == "female":
            dead_f += 1
        elif data[1] == "1" and data[4] == "male":
            sur_m += 1
        elif data[1] == "0" and data[4] == "male":
            dead_m += 1

        if data[2] == "1":
            st_class += 1
        elif data[2] == "2":
            nd_class += 1
        elif data[2] == "3":
            rd_class += 1






procent_m_and_f = procent_f + procent_m
procent_w = procent_f * 100 / procent_m_and_f
procent_M = procent_m * 100 / procent_m_and_f
survived_f = sur_f * 100 / procent_f
died_f = dead_f * 100 / procent_f
survived_m = sur_m * 100 / procent_m
died_m = dead_m * 100 / procent_m
first_class = st_class * 100 / procent_m_and_f
second_class = nd_class * 100 / procent_m_and_f
third_class = rd_class * 100 / procent_m_and_f

print(procent_w)
print(procent_M)
print(survived_f)
print(died_f)
print(survived_m)
print(died_m)
print(first_class)
print(second_class)
print(third_class)


dict = {
    "female":procent_f,
    "male":procent_m,
    "female_%":procent_w,
    "male_%":procent_M,
    "survived_female":survived_f,
    "survived_male":survived_m,
    "dead_female":dead_f,
    "dead_male":dead_m,
    "dead_female_%":died_f,
    "dead_male_%":died_m,
    "1st_class":st_class,
    "1st_class_%":first_class,
    "2nd_class":nd_class,
    "2nd_class_%":second_class,
    "3rd_class":rd_class,
    "3rd_class_%":third_class
}

#1"r"w""a""r+""a+"
#2axali file sheiqmneba
#3tupleshi indexebi araa








