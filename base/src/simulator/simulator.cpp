#include <cstring>

#include "simulator.h"

QUESTA::Simulator::Simulator() {
    this->queue_length = nullptr;
}

void QUESTA::Simulator::init(size_t n, int seed) {
    for (size_t i = 0; i < n; i++) {
        lg.addNode();
        lg.addNode();
    }
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = n; j < (n << 1); ++j) {
            lg.addEdge(lg.nodeFromId(i), lg.nodeFromId(j));
        }
    }
    this->gen.seed(seed);
    this->n = n;
    this->queue_length = new size_t[n << 1];
    if (!this->queue_length) {
        throw Err::OUT_OF_MEMORY;
    }
    memset(this->queue_length, 0, (n << 1) * sizeof(size_t));
}

QUESTA::Simulator::~Simulator() {
    if (this->queue_length) {
        delete[] this->queue_length;
    }
}
