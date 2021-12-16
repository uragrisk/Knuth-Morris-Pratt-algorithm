from kmp import build_prefix_table, find_match

if __name__ == '__main__':
    pattern = "lfds"
    input_string = "dlksjfljlfdsj"

    find_match(input_string, pattern)
