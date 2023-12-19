# Programme simple possédant du code non atteignable
level = 0

def new_level(new_val):

    if new_val < 0:
        new_val = new_val * -1

    level = new_val

    if level < 0:
        print("Code non atteignable !")

if __name__ == "__main__":
    new_level(3)