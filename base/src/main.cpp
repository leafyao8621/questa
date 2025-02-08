#include <iostream>

#include "simulator/simulator.h"

int main() {
    size_t *total_queue_length = new size_t[10];
    try {
        QUESTA::Simulator simulator;
        simulator.init(2, 1000);
        simulator(
            QUESTA::Simulator::Mode::LOG_MAX_PLUS_QUEUE_LENGTH,
            0.9,
            100,
            10,
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
    delete[] total_queue_length;
    return 0;
}
