#include "core.h"
#include "mpy_glue.h"
#include <new>          // new

extern "C" {
    #include "py/gc.h"
    #include "py/misc.h"// m_new/m_del
}

// foreward declaration of handles
struct LedWrapper { LedDriver* obj; };
struct ConsoleWrapper { Console* obj; };

static Console global_console;
static ConsoleWrapper wrapper_global_console;

// wrap cpp-functions
extern "C" {
    LedWrapper* bridge_led_new(uint32_t pin) {
        void* driver_mem = m_new(uint8_t, sizeof(LedDriver));   // allocate memory from micropython gc
        LedDriver* driver = new (driver_mem) LedDriver(pin);    // construct cpp-object in allocated space
        LedWrapper* w = m_new(LedWrapper, 1);                   // allocate memory for opaque Wrapper-Pointer
        w->obj = driver;                                        // connect Pointer to Object
        return w;
    }

    void bridge_led_delete(LedWrapper* w) {
        if (w) {
            w->obj->~LedDriver();                               // call native deinit-function
            m_del(uint8_t, w->obj, sizeof(LedDriver));          // free memory of LED-Classobj
            m_del(LedWrapper, w, 1);                            // free memory of Wrapper-Pointer
        }
    }

    void bridge_led_on(LedWrapper* w) { w->obj->turn_on(); }
    void bridge_led_off(LedWrapper* w) { w->obj->turn_off(); }
    bool bridge_led_is_on(LedWrapper* w) { return w->obj->is_on(); }
    uint32_t bridge_led_get_pin(LedWrapper* w) { return w->obj->get_pin(); }
    void bridge_led_print_status(LedWrapper* w) { w->obj->print_status(); }


    ConsoleWrapper* bridge_console_new() {
        wrapper_global_console.obj = &global_console;
        return &wrapper_global_console;
    }
    void bridge_console_delete(LedWrapper* w) {
        /*if (w) {
            delete w->obj;
            delete w;
        }*/
    }

    void bridge_console_info(ConsoleWrapper* w, const char* msg) {
        w->obj->print_debug(msg);
    }
}