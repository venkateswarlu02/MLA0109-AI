def is_valid_mapping(arr, s, mapping):
    encoded_arr = []
    for word in arr:
        num = ''
        for char in word:
            num += str(mapping.get(char, ''))
        encoded_arr.append(int(num))
    
    s_num = ''
    for char in s:
        s_num += str(mapping.get(char, ''))
    return sum(encoded_arr) == int(s_num)

def find_mapping(arr, s, mapping, index, used_digits):
    if index == len(arr) + len(s):
        return is_valid_mapping(arr, s, mapping)
    
    for digit in range(10):
        if digit not in used_digits:
            if index < len(arr):
                for char in arr[index]:
                    mapping[char] = digit
            else:
                mapping[s[index - len(arr)]] = digit
            used_digits.add(digit)
            if find_mapping(arr, s, mapping, index + 1, used_digits):
                return True
            if index < len(arr):
                for char in arr[index]:
                    if char in mapping:
                        del mapping[char]
            else:
                if s[index - len(arr)] in mapping:
                    del mapping[s[index - len(arr)]]
            used_digits.remove(digit)
    
    return False

def can_map_strings(arr, s):
    mapping = {}
    used_digits = set()
    return find_mapping(arr, s, mapping, 0, used_digits)

# Example usage:
arr = ["SEND", "MORE"]
s = "MONEY"
if can_map_strings(arr, s):
    print("Yes")
else:
    print("No")
