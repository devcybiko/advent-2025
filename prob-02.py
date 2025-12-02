def main():
    ## read input file
    dial = 50
    code = 0
    clicks = 0
    with open("./advent-01.txt.sav") as f:
        lines = f.readlines()
    for line in lines:
        ###
        n = int(line[1:])
        mod_n = n % 100
        div_n = n // 100
        delta = -1 if line[0] == "R" else 1
        ###
        clicks += div_n
        tmp = dial + delta * mod_n
        if dial != 0 and (tmp < 0 or tmp > 100):
            clicks += 1
        dial = tmp % 100
        if dial == 0:
            code += 1
            clicks += 1
    print(f"Lines: {len(lines)}, Dial: {dial}, Code: {code}, Clicks: {clicks}")
main()