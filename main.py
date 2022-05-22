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


def clean_words(_words: list[str]) -> list[str]:
    return [word.replace("\n", "").lower() for word in _words]


def name_match(name: str, _words: list[str]) -> list[str]:
    return [word for word in _words if name[0:2] in word and name[0:2] in word[-3:]]


def main(name: str):
    _word = clean_words(words())
    print(len(_word))
    matches = name_match(name, _word)
    print(matches, len(matches))


NAME_TO_CHECK = "robert".lower()

if __name__ == '__main__':
    main(NAME_TO_CHECK)
