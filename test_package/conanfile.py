from conans import ConanFile, CMake
import os

class TestTracy(ConanFile):
    generators = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(".%sexample" % os.sep)
