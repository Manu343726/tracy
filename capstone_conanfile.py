from conans import ConanFile, CMake
from conans import tools
import os

class Capstone(ConanFile):
    name = 'capstone'
    license = 'BSD'
    description = 'Capstone is a disassembly framework with the target of becoming the ultimate disasm engine for binary analysis and reversing in the security community'
    url = 'https://github.com/aquynh/capstone'

    settings = 'os', 'compiler', 'build_type', 'arch'

    _capstone_archs = {
        'ARM_SUPPORT': [True, False],
        'ARM64_SUPPORT': [True, False],
        'M680X_SUPPORT': [True, False],
        'M68K_SUPPORT': [True, False],
        'MIPS_SUPPORT': [True, False],
        'MOS65XX_SUPPORT': [True, False],
        'PPC_SUPPORT': [True, False],
        'SPARC_SUPPORT': [True, False],
        'SYSZ_SUPPORT': [True, False],
        'XCORE_SUPPORT': [True, False],
        'X86_SUPPORT': [True, False],
        'TMS320C64X_SUPPORT': [True, False],
    }

    _capstone_options = {**_capstone_archs, **{
        'ARCHITECUTRE_DEFAULT': [True, False],
        'USE_SYS_DYN_MEM': [True, False],
        'BUILD_DIET': [True, False],
        'X86_REDUCE': [True, False],
        'X86_ATT_DISABLE': [True, False],
        'BUILD_STATIC_RUNTIME': [True, False],
        'USE_DEFAULT_ALLOC': [True, False]
    }}

    options = {**_capstone_options, **{
        'shared': [True, False],
        'fPIC': [True, False]
    }}

    default_options = {
        'ARM_SUPPORT': True,
        'ARM64_SUPPORT': True,
        'M680X_SUPPORT': True,
        'M68K_SUPPORT': True,
        'MIPS_SUPPORT': True,
        'MOS65XX_SUPPORT': True,
        'PPC_SUPPORT': False,
        'SPARC_SUPPORT': True,
        'SYSZ_SUPPORT': True,
        'XCORE_SUPPORT': True,
        'X86_SUPPORT': True,
        'TMS320C64X_SUPPORT': True,
        'ARCHITECUTRE_DEFAULT': True,
        'USE_SYS_DYN_MEM': True,
        'BUILD_DIET': False,
        'X86_REDUCE': True,
        'X86_ATT_DISABLE': True,
        'BUILD_STATIC_RUNTIME': True,
        'USE_DEFAULT_ALLOC': True,
        'shared': False,
        'fPIC': True
    }

    @property
    def cmake_options(self):
        capstone_options = {f'CAPSTONE_{option}': self.options.get_safe(option) for option in self._capstone_options.keys()}
        extra_options = {
            'CAPSTONE_BUILD_STATIC': not self.options.shared,
            'CAPSTONE_BUILD_SHARED': self.options.shared,
            'CAPSTONE_BUILD_TESTS': False,
            'CAPSTONE_BUILD_CSTOOL': False
        }

        return {**capstone_options, **extra_options}

    @property
    def source_dir(self):
        return os.path.join(self.source_folder, f'{self.name}-{self.version}')

    def source(self):
        tools.get(url=f'https://github.com/aquynh/capstone/archive/{self.version}.tar.gz')

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(defs=self.cmake_options, source_dir=self.source_dir)
        cmake.build()

    def package(self):
        self.copy('*.h', dst='include')
        self.copy('*.a', dst='lib')
        self.copy('*.lib', dst='lib')
        self.copy('*.so', dst='lib')
        self.copy('*.dll', dst='lib')

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.extend([f'CAPSTONE_HAS_{arch}' for arch in self._capstone_archs])
        self.cpp_info.defines.extend([f'CAPSTONE_{arch}_SUPPORT' for arch in self._capstone_archs])
        self.cpp_info.defines.extend([f'CAPSTONE_{option}' for option in self._capstone_options])

