// print a triangle with * characters

#include <iostream>

int main() {

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10 - i; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < i * 2 + 1; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    
}