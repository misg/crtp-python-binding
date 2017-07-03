import importlib
import subprocess
import json
import sys
import os

def load_includes(impl_t):
  with open('config.json', 'r') as config_f:
    conf = json.loads(config_f.read())
    result = ""
    if impl_t in conf:
      for incl in conf[impl_t]:
        result += '#include "' + incl + '"\n'
    return result

def write_pybind11_module(impl_t):
  with open('bindings.cc', 'w') as module:
    module.write('#include "bindings.h"\n')
    module.write(load_includes(impl_t))
    module.write('\n')
    module.write('PYBIND11_MODULE(bindings' + impl_t + ', m) {\n')
    module.write('  register_interface<Interface<' + impl_t + '>>(m);\n')
    module.write('  pybind11::class_<' + impl_t + ', Interface<' + impl_t +
      '>>(m, "' + impl_t + '")\n')
    module.write('    .def(pybind11::init<>());\n')
    module.write('}\n')

def gen(impl_t):
  write_pybind11_module(impl_t)
  cmake = subprocess.Popen(["cmake", "."], cwd=os.getcwd())
  cmake.wait()
  cmake = subprocess.Popen(["cmake", "--build", ".", "--target", "bindings"], cwd=os.getcwd())
  cmake.wait()
  name = "bindings" + impl_t
  os.rename("bindings.cpython-36m-x86_64-linux-gnu.so", str(name + ".so"))
  return importlib.import_module(name)
