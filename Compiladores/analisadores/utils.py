from time import sleep

dots = [".", "..", "..."]

def print_result(message, time, result, append=""):
    print(f"\n\033[0;32m{message}\033[0;0m")

    for i in range(0, 2):
        print("Aguarde", dots[i], end="\r")
        sleep(1)

    if (type(result) == list and len(result) > 0):
        for r in result:
            print(r)
    else:
        print(result) if result else print(append)
