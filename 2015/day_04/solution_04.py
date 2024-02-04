import hashlib

input = "bgvyzdsv"

def main(input:str, n:int = 5):
    n_zeros = "0"*n
    case_found = False
    i = 0
    while case_found is False:
        hash = hashlib.md5(f"{input}{i}".encode())
        if (hash.hexdigest())[:n] == n_zeros:
            case_found = True
        else:
            i += 1

    print(f"The lowest integer that produces the desired has is {i}.")
    print(f"The produced has is {hash}.")
    return

if __name__ == "__main__":
    print("Part 1")
    main(input= input, n = 5)
    print("Part 2")
    main(input= input, n = 6)