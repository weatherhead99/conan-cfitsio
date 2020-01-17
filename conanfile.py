from conans import ConanFile, CMake, tools
import os

class CfitsioConan(ConanFile):
    name = "cfitsio"
    version = "3.470"
    license = "ISC"
    author = "Dan Weatherill (plasteredparrot@gmail.com)"
    url = "https://github.com/weatherhead99/conan-cfitsio"
    homepage = "https://heasarc.gsfc.nasa.gov/fitsio/"
    description = "a library for reading and writing data files in FITS data format"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False],  "https_support" : [True, False]}
    default_options = "shared=False", "fPIC=True", "https_support=True"
    generators = "cmake_paths"
    requires = "libcurl/7.67.0"

    _sha256sums = {"3.470"  :"985606e058403c073a68d95be74e9696f0ded9414520784457a1d4cba8cca7e2"}

    _source_subfolder = "source_subfolder"
    
    @property
    def file_version(self):
        versparts = self.version.split(".")
        versparts[1] = versparts[1].strip("0")
        return ".".join(versparts)

    def config_options(self):
        #https support only available on non-windows platforms
        if self.settings.os == "Windows":
            del self.options.https_support

        #no fPIC on visual studio
        if self.settings.compiler == "Visual Studio":
            del self.options.fPIC
    
    def configure(self):
        #C only library
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = "conan_paths.cmake"
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder=self._source_subfolder)
        return cmake
        
    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = "%s-%s" % (self.name, self.file_version)
        os.rename(extracted_dir, self._source_subfolder)
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        
    def package(self):
        cmake  = self._configure_cmake()
        cmake.install()
        self.copy(pattern="Licence.txt", dst="licenses", src=self._source_subfolder) 

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

