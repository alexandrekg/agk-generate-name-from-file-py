import random

def clean_name(_name):
    return _name.replace("\n", "")


def get_names(names_file):
    _names = []
    for _name in names_file:
        _name = clean_name(_name)
        _names.append(_name)

    return _names


def main():
    with open('names.txt') as names_file:
        names_list = get_names(names_file)

    random_name = random.choice(names_list)
    print(f"Nome gerado automaicamente: {random_name}")


if __name__ == "__main__":
    main()