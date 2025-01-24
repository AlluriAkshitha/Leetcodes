#include <stdlib.h>

int* evenOddBit(int n, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int)); // Allocate memory for the result array
    result[0] = 0; 
    result[1] = 0; 
    
    int index = 0; 
    
    while (n > 0) {
        if (n & 1) { 
            if (index % 2 == 0) {
                result[0]++; 
            } else {
                result[1]++; 
            }
        }
        n >>= 1; 
        index++; 
    }
    
    *returnSize = 2; 
    return result;
}
