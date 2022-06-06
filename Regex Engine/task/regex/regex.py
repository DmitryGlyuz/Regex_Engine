def match_chars(re_char: str, char: str) -> bool:
    return re_char == char or char and re_char == '.'


def match_pattern(pattern: str, string: str) -> bool:
    def first_char_match():
        return bool(pattern) and bool(string) and match_chars(pattern[0], string[0])

    if not (len(pattern) > 1 and pattern[0] != '\\' and pattern[1] in '?*+'):
        if pattern and pattern[0] == '\\':
            pattern = pattern[1:]
        return not pattern or first_char_match() and (
                len(pattern) == 1 or
                (len(string) == 1 and pattern[1:] == '$') or
                match_pattern(pattern[1:], string[1:]))
    match pattern[1]:
        case '?':
            return match_pattern(pattern[2:], string) or (first_char_match() and match_pattern(pattern[2:], string[1:]))
        case '*':
            return match_pattern(pattern[2:], string) or len(string) > 0 and match_pattern(pattern, string[1:])
        case '+':
            return first_char_match() and (match_pattern(pattern[2:], string[1:]) or match_pattern(pattern, string[1:]))


def initial_match(pattern: str, string: str) -> bool:
    if not pattern:
        return True
    elif pattern[0] == '^':
        return match_pattern(pattern[1:], string)
    for start_index in range(0, len(string)):
        if match_pattern(pattern, string[start_index:]):
            return True
    return False


def check_input(user_input: str) -> bool:
    return initial_match(*user_input.split('|'))


if __name__ == '__main__':
    print(check_input(input()))
d