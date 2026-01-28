year_born = []
countries_set = set()


with open("clients.txt", "r") as file:
    with open("spain_germany.txt", "w") as file2:
        for line in file:
            line = line.strip()
            parts = line.split(";")

            countries_set.add(parts[2].strip())

            if parts[2] == "Spain" or parts[2] == "Germany":
                file2.write(parts[0] + "\n")

            year_born = []
            i = parts[3].strip()
            j = i.split("/")
            if j[2] == "2011":
                year_born.append(parts[1])
                print(year_born)
countries = list(countries_set)
print("Countries:", countries)
