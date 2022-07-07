"""
 This program encodes user input into binary data!
 Your job is to write the textToBinary function
"""

def text_to_binary(text):
    
    # Write this method!
    """
    a_byte_array = bytearray(text, "utf8")
    
    byte_list = []
    
    for byte in a_byte_array:
        binary_representation = bin(byte)
    
    byte_list.append(binary_representation)
    print(bin(str(byte_list))[2:])
    """
    return (''.join(format(ord(x), 'b') for x in text))

    # For every character in the text,
        # convert the character into its ASCII decimal encoding
        # then convert that decimal value into its equivalent binary encoding
        # and combine each binary encoding to get the resulting binary string


# Converts a given decimal value into an 8 bit binary value
def decimal_to_binary(decimal_value):
    binary_base = 2
    num_bits_desired = 8
    binary_value = str(bin(decimal_value))[2:]
    
    while len(binary_value) < num_bits_desired:
        binary_value = "0" + binary_value
    
    return binary_value

text = input("Input the string you would like to encode: ")
binary = text_to_binary(text)

print(binary)