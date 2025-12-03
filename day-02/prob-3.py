def is_bad_id(id):
    s = str(id)
    s0 = s[0:len(s)//2]
    s1 = s[len(s)//2:]
    return s0 == s1

def main():
    ## read input file
    with open("./input.txt") as f:
        input = f.readlines()[0]
    lines = [line.strip() for line in input.split(",")]
    print(lines)
    sum = 0
    for line in lines:
        words = line.split("-")
        start = int(words[0])
        end = int(words[1])
        for i in range(start, end+1):
            if (is_bad_id(i)):
                print("bad id", i)
                sum += i
    print(sum)
main()
