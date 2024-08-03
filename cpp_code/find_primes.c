#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

    const int bound = 1e6;                              /* upper bound to compute primes */
    int *primes = (int*) calloc(bound, sizeof(int));    /* array of primes, it could be more memory-efficient */
                                                        /* and allocate an array of side log(bound)/bound, but anyway */
    int size = 1;                                       /* number of primes found */
    primes[0] = 2;

    /* find primes less than bound */
    for(int a = 3; a < bound; ++a) {
        int i = 0;
        bool is_prime = true;
        bool is_bigger_than_sqrt = false;
        while(i < size && is_prime && !is_bigger_than_sqrt) {
            int p = primes[i];
            is_prime = !(a % p == 0);
            is_bigger_than_sqrt = (p > (int) floor(sqrt(a)));
            i++;
        }
        if(is_prime && is_bigger_than_sqrt) {
            primes[size] = a;
            size++;
        }
    }

    /* save to file named filename */
    char filename[256];
    sprintf(filename, "../data/prime_numbers/primes_%d.txt", bound);
    FILE *fptr = fopen(filename, "w");
    for(int i = 0; i < size; ++i) {
        fprintf(fptr, "%d\n", primes[i]);
    }
    fclose(fptr);
}