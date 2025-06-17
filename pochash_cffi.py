import cffi

# Create a cffi interface
ffi = cffi.FFI()

# Define the function signature
ffi.cdef("void hash(const char* input, char** output);")

# Load the shared library
libhash = ffi.dlopen("./libhash.so")

# Create a Python function that wraps the C function
def hash(input_str):
    input_bytes = input_str.encode('utf-8')
    output_ptr = ffi.new("char**")
    libhash.hash(input_bytes, output_ptr)
    output_bytes = ffi.string(output_ptr[0]).decode('utf-8')
    return output_bytes

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) > 1:
        print(hash(argv[1]))
        exit(0)
    print(f'please use: {argv[0]} <message>')
