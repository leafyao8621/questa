#include <iostream>

#include "simulator/simulator.h"

int main() {
    int *total_queue_length = new int[1000000];
    try {
        QUESTA::Simulator simulator;
        simulator.init(2, 1000);
        simulator(
            QUESTA::Simulator::Mode::LOG_MAX_PLUS_QUEUE_LENGTH,
            0.9,
            1000000,
            1000000,
            total_queue_length
        );
    } catch (QUESTA::Simulator::Err err) {
        delete[] total_queue_length;
        switch (err) {
        case QUESTA::Simulator::Err::OUT_OF_MEMORY:
            std::cerr << "OUT OF MEMORY" << std::endl;
            break;
        case QUESTA::Simulator::Err::NOT_IMPLEMENTED:
            std::cerr << "NOT IMPLEMENTED" << std::endl;
            break;
        }
        return -1;
    }
    for (size_t i = 0; i < 1000000; ++i) {
        std::cout << total_queue_length[i] << std::endl;
    }
    delete[] total_queue_length;
    return 0;
}
