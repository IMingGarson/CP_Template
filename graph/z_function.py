def calculate_z_values(s):
    """
    Calculate the Z values for the given string.

    Args:
    s (str): The input string.

    Returns:
    list: A list of Z values for each position in the input string.
    """
    n = len(s)
    z_values = [0] * n
    l, r = 0, 0  # Left and right pointers
    for i in range(1, n):
        if i <= r:
            z_values[i] = min(r - i + 1, z_values[i - l])
        while i + z_values[i] < n and s[z_values[i]] == s[i + z_values[i]]:
            z_values[i] += 1
        if i + z_values[i] - 1 > r:
            l, r = i, i + z_values[i] - 1
    return z_values
