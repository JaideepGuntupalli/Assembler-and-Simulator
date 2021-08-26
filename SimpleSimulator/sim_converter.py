# This file is for handling conversions between binary and decimals

# ----- Decimal -> Binary [START]-----

def bin(dec_int):
    if dec_int == 0:
        return 0
    else:
        return (dec_int % 2 + 10 * bin(int(dec_int // 2)))


def dectobin(dec_str):

    return format(int(dec_str), "016b")

    dec_int = int(dec_str)

    bin_int = bin(dec_int)

    bin_str = str(bin_int)

    bin_str_ans = ""

    bin_str_ans += (8 - len(bin_str)) * "0"

    bin_str_ans += bin_str

    return bin_str_ans

# ----- Decimal -> Binary [END]-----

# ----- Binary -> Decimal [START]-----

def dec(bin_str, i = 0):
    
    bin_len = len(bin_str)

    if i == bin_len - 1:
        return int(bin_str[i]) - 0

    else:
        return (((int(bin_str[i]) - 0) << (bin_len - i - 1)) + dec(bin_str, i + 1))

def bintodec(bin_str):

    dec_int = dec(bin_str)
    
    return dec_int

# ----- Binary -> Decimal [END]-----



