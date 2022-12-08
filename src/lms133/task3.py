from to_do import TODO

def converter(hours):
    return hours * 60 * 60 * 1000


if __name__ == "__main__":
    print(converter(1))
