
"""
This script generates a pseudo random binary sequence for a given degree, bitmask and seed value
    The degree of the polynomial must be between 1 and 32. 
    Degree is just a fancy way of specifying the size of the LFSR i.e. 
    degree 7 represents a 7 bit LFSR and consequently an LFSR with degree 7 
    will produce a maximal length sequence of 2^7-1 == 127. Bitmask affects 
    the next state of the LFSR i.e. it specifies the bit positions. 
    For example: in our case 
    We need a particular 127 bit sequence. We can use this poylnomial to 
    represent our bitmask x^7 + x^6 + x^5 + x^4. 
    The powers of the polynomial terms represent the bits in your bitmask. 
    So, this bit mask in binary would be '1111000' or in decimal - '120' 
    Seed is the initial value of the shift register - in our case its decimal value is '80'

"""

# Check out the examples in examples_glfsr.py for more.


def glfsr_length_check(degree):
    if (degree < 1 or degree > 32):
        raise ValueError("Error: degree must be between 1 and 32 inclusive")
    return True


def glfsr(degree, mask, seed):
    if (glfsr_length_check(degree)):
        wq = []
        d_shift_register = seed
        for i in range(2**degree-1):
            # For a given state of the LFSR - check if the LSB (i.e. 'bit'variable) in the shift register is 1.
            bit = d_shift_register & 0x1
            # This operation will output either a 1 or a zero and is essentially the output
            # of the LFSR

            d_shift_register >>= 1           # Shift all bits in the register by 1 to the right
            if (bit):                        # If LSB in the shift register (i.e. variable 'bit') is 1
                # Then XOR the shift register with the bitmask and change state for next round.
                d_shift_register ^= mask
            # Output is appended to pseudo random sequence of bits.
            wq.append(bit)
        return wq
