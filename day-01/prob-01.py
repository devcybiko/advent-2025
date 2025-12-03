def main():
    ## read input file
    dial = 50
    code = 0
    with open("./advent-01.txt") as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())
        if line[0] == "L":
            dial += int(line[1:])
        elif line[0] == "R":
            dial -= int(line[1:])
        dial = dial % 100
        if dial == 0:
            code += 1
    print(f"Lines: {len(lines)}, Dial: {dial}, Code: {code}")
main()