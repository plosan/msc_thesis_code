#include <vector>
#include <utility>
#include <iostream>
#include <string>

bool is_mu_constant_deformation(const int a, const int b, std::vector<std::pair<int, int>> exp_def) {
    for(auto exp_pair : exp_def) {
        int ab = a * b;
        int sum = a * exp_pair.second + b * exp_pair.first;
        if(sum <= ab)
            return false;
    }
    return true;
}

std::string bool_to_string(const bool b) {
    return (b ? std::string("true") : std::string("false"));
}

int main(int argc, char* argv[]) {

    int a = 4;
    int b = 5;

    int alpha = 2;
    int beta = 3;

    std::pair<int, int> exp_mon_1(alpha, beta);

    std::vector<std::pair<int, int>> exp_def(1);
    exp_def[0] = exp_mon_1;

    bool is_def = is_mu_constant_deformation(a, b, exp_def);

    std::cout << bool_to_string(is_def) << std::endl;


}