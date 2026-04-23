#pragma once

#include <stdint.h> 
#include <stdbool.h> 
#include <stdarg.h> 
#include <cstdio>   //printf
#include "pico/stdlib.h" 
#include "hardware/gpio.h"

class Console {
public:
    Console();

    void print_debug(const char* message) const;
};

class LedDriver {
public:
    LedDriver(uint32_t pin);
    ~LedDriver();

    void turn_on();
    void turn_off();
    bool is_on() const;
    uint32_t get_pin() const;
    void print_status() const;

private:
    uint32_t pin_;
};
