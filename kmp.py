def build_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            prefix_table[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix_table[i] = 0
                i += 1
            else:
                j = prefix_table[j - 1]
    return prefix_table


def find_match(string, pattern):
    pi = build_prefix_table(pattern)
    string_len = len(string)
    pattern_len = len(pattern)
    i = 0
    j = 0
    while i < string_len:
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == pattern_len:
                print(f'pattern "{pattern}" was found in string '
                      f'{string[:i - pattern_len]}-->{string[i - pattern_len:i]}<--'
                      f'{string[i:string_len]}')
                return True

        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    if i == string_len:
        print("not found")
        return False
