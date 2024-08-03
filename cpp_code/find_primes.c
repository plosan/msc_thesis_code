#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <climits>

int main(int argc, char* argv[]) {

    int bound = 1e6;

    std::vector<int> primes(1);
    primes[0] = 2;

    for(int a = 3; a < bound; ++a) {
        int i = 0;
        int sz = int(primes.size());
        bool is_prime = true;
        bool is_less_than_sqrt = true;
        while(i < sz && is_prime && is_less_than_sqrt) {
            int p = primes[i];
            is_prime = !(a % p == 0);
            is_less_than_sqrt = (p < int(sqrt(a)));
            i++;
        }
        if(is_prime)
            primes.push_back(a);
    }

    std::fstream file("primes.txt");
    if(file.is_open()) {
        for(int i = 0; i < int(primes.size()); ++i) {
            file << primes[i] << std::endl;
        }
    }
    file.close();


}