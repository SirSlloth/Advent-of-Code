import os

def main():
    x = x1 = x2 = 0
    y = y1 = y2 = 0
    
    path = {(0,0):1}
    paired_path = {(0,0):2}
    with open(os.path.dirname(os.path.realpath(__file__)) + "/input_day_03.txt", mode = "r") as i:
        directions = i.read()

    for c,char in enumerate(directions):
        match char:
            case ">":
                x += 1
            case "<":
                x -= 1
            case "^":
                y += 1
            case "v":
                y -= 1
        
        key = (x,y)
        if key in path:
            path[key] = path[key] + 1
        else:
            path[key] = 1
    #Part 2 calcualtions
        if c % 2 == 0:
            match char:
                case ">":
                    x1 += 1
                case "<":
                    x1 -= 1
                case "^":
                    y1 += 1
                case "v":
                    y1 -= 1

            key = (x1,y1)
            if key in paired_path:
                paired_path[key] = paired_path[key] + 1
            else:
                paired_path[key] = 1 

        else:
            match char:
                case ">":
                    x2 += 1
                case "<":
                    x2 -= 1
                case "^":
                    y2 += 1
                case "v":
                    y2 -= 1

            key = (x2,y2)
            if key in paired_path:
                paired_path[key] = paired_path[key] + 1
            else:
                paired_path[key] = 1 


    ans1 = len(path)
    ans2 = len(paired_path)
    print(f"In total Santa visited {ans1} houses.")
    print(f"In total Sant and Robo-Santa visited {ans2} houses.")
    return

if __name__ == "__main__":
    main()