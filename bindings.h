#ifndef CRTP_BINDINGS_H_
#define CRTP_BINDINGS_H_

#include <pybind11/pybind11.h>
#include "interface.h"

template<class Interface>
void register_interface(const pybind11::module& m) {
  pybind11::class_<Interface>(m, "Interface")
    .def(pybind11::init<>())
    .def("print", &Interface::print);
}

#endif // CRTP_BINDINGS_H_
