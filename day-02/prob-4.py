def is_bad_id(id):
    s = str(id)
    for i in range(1, len(s)//2+1):
        s0 = s[0:i]
        if (s == s0 * (len(s)//i)):
            print("bad id", s, i)
            return True
    return False

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
                sum += i
    print(sum)
main()
