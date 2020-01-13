from conans import ConanFile, CMake, tools


class CfitsioConan(ConanFile):
    name = "cfitsio"
    version = "3.470"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Cfitsio here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "https_support" : [True, False]}
    default_options = {"shared": False, "https_support" : True}
    generators = "cmake_paths"
    requires = "libcurl/7.67.0"

    @property
    def file_version(self):
        versparts = self.version.split(".")
        versparts[1] = versparts[1].strip("0")
        return ".".join(versparts)

    def config_options(self):
        #https support only available on non-windows platforms
        if self.settings.os == "Windows":
            del self.options.https_support
    
    def configure(self):
        #C only library
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd
    
    def source(self):
        SHA256SUM = "985606e058403c073a68d95be74e9696f0ded9414520784457a1d4cba8cca7e2"
        URL = "http://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/%s-%s.tar.gz" \
              % (self.name, self.file_version)
        tools.get(URL,sha256=SHA256SUM)
        
    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = "conan_paths.cmake"
        cmake.configure(source_folder="%s-%s" % (self.name, self.file_version))
        cmake.build()
        cmake.install()
        
    def package(self):
        pass
    
    def package_info(self):
        self.cpp_info.libs = ["hello"]

