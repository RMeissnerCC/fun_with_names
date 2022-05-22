# Script to find all words, that somehow lead to Robert - my name, e.g. Euro.
# Some friends of mine create funny nicknames from such names
import os


def words_from_file(filepath: str, path: str) -> list[str]:
    with open(f"{path}/{filepath}", encoding="Latin-1") as file:
        return file.readlines()


def words() -> list[str]:
    _output = []
    [_output.extend(words_from_file(filepath, "data")) for filepath in os.listdir("data")]
    return _output


def main():
    _word = words()
    print(_word)


if __name__ == '__main__':
    main()
