import os

def part_1(input = str) -> int:
    up = input.count("(")
    down = input.count(")")
    destination = up-down
    return destination


def part_2(input:str) -> int:
    current_floor = 0
    for c,i in enumerate(input):
        match i:
            case "(":
                current_floor += 1
            case ")":
                current_floor += -1
        if current_floor <0:
            return c + 1
    return 0

def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(file_path, "input.txt")
    with open(input_path) as r:
        input = r.read()
    
    part_1_ans = part_1(input)
    print(part_1_ans)

    part_2_ans = part_2(input)
    print(part_2_ans)    
    return

if __name__ ==  "__main__":
    main()
