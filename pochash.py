import ctypes

# Load the shared library
libhash = ctypes.CDLL('./libhash.so')

# Define the function signature
libhash.hash.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
libhash.hash.restype = None

# Create a Python function that wraps the C function
def hash(input_str):
    input_bytes = input_str.encode('utf-8')
    output_ptr = ctypes.pointer(ctypes.c_char_p())
    libhash.hash(input_bytes, output_ptr)
    output_bytes = output_ptr.contents.value
    return output_bytes.decode('utf-8')

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) > 1:
        print(hash(argv[1]))
        exit(0)
    print(f'please use: {argv[0]} <message>')
