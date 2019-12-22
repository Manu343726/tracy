from conans import ConanFile, CMake

class Tracy(ConanFile):
    name = 'tracy_client'
    version = 'master'
    license = 'BSD'
    description = 'A real time, nanosecond resolution, remote telemetry frame profiler for games and other applications'
    url = 'https://bitbucket.org/Manu343726/tracy/src/master'

    exports_sources = '*.cpp', '*.hpp', '*.h', 'CMakeLists.txt'

    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'TRACY_ENABLE': [True, False]}
    default_options = {'TRACY_ENABLE': True}

    def build(self):
        cmake = CMake(self)
        cmake.configure(defs={'TRACY_ENABLE': self.options.TRACY_ENABLE})
        cmake.build()

    def package(self):
        self.copy('*.h', dst='include')
        self.copy('*.hpp', dst='include')
        self.copy('*.a', dst='lib')
        self.copy('*.lib', dst='lib')

    def package_info(self):
        self.cpp_info.libs = ['tracy_client']

        if self.options.TRACY_ENABLE:
            if not self.settings.os == 'Windows':
                self.cpp_info.cxxflags = ['-pthread']
                self.cpp_info.system_libs = ['dl', 'pthread']

            self.cpp_info.defines = ['TRACY_ENABLE']
