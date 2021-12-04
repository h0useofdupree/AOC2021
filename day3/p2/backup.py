for i in range(2):
        for pos in range(12):
            print(len(lines))
            count_of_1 = 0
            count_of_0 = 0

            for line in lines:
                if int(line[pos]) == 1:
                    count_of_1 += 1
                elif int(line[pos]) == 0:
                    count_of_0 += 0

            if count_of_1 > count_of_0:
                for line in lines:
                    if line.startswith(str(i)) is True:
                        lines.remove(line)
            elif count_of_0 > count_of_1:
                for line in lines:
                    if line.startswith(str(i)) is True:
                        lines.remove(line)
            print(len(lines))
        if i == 0:
            oxyStr = "".join(map(str, lines))
        else:
            co2Str = "".join(map(str, lines))
    return (oxyStr, co2Str)