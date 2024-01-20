import os

def main():
    ans1 = 0
    ans2 = 0 
    with open(os.path.dirname(os.path.realpath(__file__)) + "/input_day_02.txt", mode = "r") as i:
        lines = i.readlines()
    for l in lines:
        d1, d2, d3 = map(int, l.split("x"))
        s = [(d1*d2), (d2*d3), (d1*d3)]
        p = [(d1+d2)*2,(d1+d3)*2,(d2+d3)*2]
        t = 2*(s[0] + s[1] + s[2]) + (min(s))
        r = min(p) + (d1*d2*d3)
        ans1 += t
        ans2 += r
    print(f"The elves need to order {ans1} feet of wrapping paper.")
    print(f"The elves need to order {ans2} feet of ribbon.")
    return

if __name__ == "__main__":
    main()