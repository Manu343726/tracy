from conans import ConanFile, AutoToolsBuildEnvironment
import os


class TracyServer(ConanFile):
    name = 'tracy_server'
    version = 'master'
    license = 'BSD'
    description = 'A real time, nanosecond resolution, remote telemetry frame profiler for games and other applications'
    url = 'https://bitbucket.org/Manu343726/tracy/src/master'
    exports_sources = '*'
    settings = 'os', 'compiler', 'build_type', 'arch'

    requires = ('freetype/2.10.2',
                'glfw/3.3.2',
                'capstone/4.0.2')

    @property
    def build_dir(self):
        return os.path.join(self.source_folder, 'profiler', 'build', 'unix')

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        cwd = os.getcwd()
        autotools.make(target='release', args=['-C', self.build_dir])

    def package(self):
        self.copy('Tracy-*', src=self.build_dir, dst='bin', keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
