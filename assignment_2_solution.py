def modify_string(s):
    n = len(s)
    ascii_values = [ord(char) for char in s]
    modified = set()

    for i in range(n):
        if ascii_values[i] % 2 == 0:
            if i + 1 < n:
                new_ascii = (ascii_values[i + 1] + ascii_values[i] % 7) % 128
                ascii_values[i + 1] = new_ascii
        else:
            if i > 0:
                new_ascii = (ascii_values[i - 1] - ascii_values[i] % 5) % 128
                ascii_values[i - 1] = new_ascii

    for i in range(n):
        if ascii_values[i] < 0 or ascii_values[i] > 127:
            ascii_values[i] = 83

    new_string = ''.join(chr(ascii_val) for ascii_val in ascii_values)
    return new_string

s = "sHQen}"
output = modify_string(s)
print(output) 
