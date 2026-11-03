"""converter.py · number-system-toolkit
Convert between decimal, binary, hex and any base 2-16, written by hand.
"""

def decimal_to_binary(n):
    """13 -> '1101'"""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        remainder = n % 2           # what's left over after dividing by 2
        bits = bits + str(remainder)
        n = n // 2                  # divide by 2, drop the decimal part
    return bits[::-1]               # remainders came out backwards, so flip them


def binary_to_decimal(s):
    """'1101' -> 13"""
    total = 0
    for position, digit in enumerate(reversed(s)):
        if digit not in "01":
            raise ValueError(f"{s} is not binary")
        total = total + int(digit) * 2 ** position   # digit x its place value
    return total


if __name__ == "__main__":
    print(decimal_to_binary(13))
    print(decimal_to_binary(0))
    print(binary_to_decimal("1101"))
    print(binary_to_decimal("11111111"))
