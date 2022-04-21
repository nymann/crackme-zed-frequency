def zed_frequency(user_key: str, max_key_length: int = 26) -> bool:
    key_matrix = [0 for _ in range(max_key_length)]
    for char in user_key:
        if not char.isalpha():
            continue
        if char.isupper():
            minus = ord("A")
        else:
            minus = ord("a")
        key_matrix[ord(char) - minus] += 1
    key = _generate_key_from_key_matrix(key_matrix=key_matrix)
    return key == "01234567890123456789012345"


def _generate_key_from_key_matrix(key_matrix: list[int]) -> str:
    key_list: list[str] = []
    for key in key_matrix:
        char = chr(key + ord("0"))
        key_list.append(char)
    return "".join(key_list)
