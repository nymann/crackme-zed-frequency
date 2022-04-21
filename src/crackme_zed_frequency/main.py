import random

import typer

app = typer.Typer()


def generate_key() -> str:
    key = ""
    check = "01234567890123456789012345"
    for index, char in enumerate(check):
        to_add = chr(ord("a") + index)
        for _ in range(int(char)):  # noqa: WPS519
            key += to_add
    return key


def make_key_look_legit(key: str) -> str:
    key_list: list[str] = list(key)
    random.shuffle(key_list)
    final_key: str = ""
    for char in key_list:
        if bool(random.getrandbits(1)):
            final_key += char.upper()
        else:
            final_key += char.lower()
    return final_key


@app.command()
def keygen() -> None:
    valid_key = generate_key()
    shuffled = make_key_look_legit(key=valid_key)
    typer.echo(shuffled)


if __name__ == "__main__":
    app()
