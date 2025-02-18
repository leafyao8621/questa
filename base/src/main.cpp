#include <iostream>

#include "runner/runner.h"

// double s[54] = {
//     0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.91, 0.92,
//     0.93, 0.94, 0.95, 0.96, 0.961, 0.962, 0.963, 0.964, 0.965,
//     0.966, 0.967, 0.968, 0.969, 0.97, 0.971, 0.972, 0.973,
//     0.974, 0.975, 0.976, 0.977, 0.978, 0.979, 0.98, 0.981,
//     0.982, 0.983, 0.984, 0.985, 0.986, 0.987, 0.988, 0.989,
//     0.99, 0.991, 0.992, 0.993, 0.994, 0.995, 0.996, 0.997,
//     0.998, 0.999
// };

int main() {
    int *total_queue_length = new int[100];
    try {
        QUESTA::Simulator simulator;
        simulator.init(2, 1000);
        simulator(
            QUESTA::Simulator::Mode::MAX_WEIGHT,
            0.9,
            10000,
            100,
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
    for (size_t i = 0; i < 100; ++i) {
        std::cout << total_queue_length[i] << std::endl;
    }
    delete[] total_queue_length;
    return 0;
}
