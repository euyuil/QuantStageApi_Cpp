import os
import shutil
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class QuantStageApiConan(ConanFile):

    name = "QuantStageApi"
    version = "20190107"

    # https://docs.conan.io/en/latest/reference/conanfile/attributes.html#settings
    settings = {
        'os': ['Linux', 'Windows'],
        'arch': ['x86_64'],
        'build_type': ['Release'],
        'compiler': {
            'gcc': {'version': ['4.8', '5', '5.4']},
            'Visual Studio': {'version': ['12']}
        }
    }

    # requires = 'boost/1.64.0@conan/stable'
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    exports_sources = 'bin/*', 'include/*'

    def build(self):
        # https://docs.conan.io/en/latest/mastering/conditional.html
        if self.settings.os == 'Linux':
            if self.settings.compiler.version == '4.8':
                tools.unzip('bin/linux-gcc4.8.zip')
                shutil.move('linux-gcc4.8/QuantBaseApi/libprotobuf.so.13.0.0', 'linux-gcc4.8/QuantBaseApi/libprotobuf.so.13')
            elif self.settings.compiler.version in ['5', '5.4']:
                tools.unzip('bin/linux-gcc5.4.zip')
                shutil.move('linux-gcc5.4/QuantBaseApi/libprotobuf.so.13.0.0', 'linux-gcc5.4/QuantBaseApi/libprotobuf.so.13')
        elif self.settings.os == 'Windows':
            if self.settings.compiler.version == '12':
                tools.unzip('bin/lib-x64-msvc-12.0-Release.zip')

    def package(self):
        self.copy('*.h', dst='include', src='include')
        # self.copy('*.so*', dst='lib', keep_path=False, excludes='*boost*')
        self.copy('*.so*', dst='lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.LD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
        self.env_info.DYLD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
