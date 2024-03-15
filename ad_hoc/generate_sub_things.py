def generate_subarrays_except_for_empty_array(arr):
    return [arr[i:j] for i in range(len(arr)) for j in range(i + 1, len(arr) + 1)]

def generate_substrings_except_for_empty_string(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
