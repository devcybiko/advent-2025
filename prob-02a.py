def main():
    ## read input file
    dial = 50
    code = 0
    clicks = 0
    with open("./advent-01.txt") as f:
        lines = f.readlines()
    for line in lines:
        n = int(line[1:])
        delta = -1 if line[0] == 'R' else 1
        for i in range(0, n):
            dial = (dial + delta) % 100
            if dial == 0: clicks += 1
        if dial == 0:
            code += 1
    print(f"Lines: {len(lines)}, Dial: {dial}, Code: {code}, Clicks: {clicks}")
main()