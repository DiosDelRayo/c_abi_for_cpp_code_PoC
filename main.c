#include <stdint.h>
#include <stdio.h>
#include "hash.h"

int main() {
    char bytes[] = "Hola";
    char* output = NULL;
    hash(bytes, &output);

    printf("Hash: %s\n", output);
    return 0;
}
