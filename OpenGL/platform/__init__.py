"""Abstraction for the platform-specific code in PyOpenGL

Each supported platform has a module which provides the
specific functionality required to support the base OpenGL 
functionality on that platform.  These modules are 
registered using plugins in the:

    OpenGL.plugin.PlatformPlugin

objects.  To support a new platform you'll need to create
a new PlatformPlugin instance *before* you import 
OpenGL.platform .  Once you have a working platform 
module, please consider contributing it back to the project.

See baseplatform.BasePlatform for the core functionality 
of a platform implementation.  See the various platform 
specific modules for examples to use when porting.
"""
import os, sys
from OpenGL.plugins import PlatformPlugin

def _load( ):
    """Load the os.name plugin for the platform functionality"""
    key = (os.environ.get( 'PYOPENGL_PLATFORM'), sys.platform,os.name)
    plugin  = PlatformPlugin.match( key )
    plugin_class = plugin.load()
    plugin.loaded = True
    # create instance of this platform implementation
    plugin = plugin_class()

    # install into the platform module's namespace now
    plugin.install(globals())
    return plugin

_load()

def types(resultType,*argTypes):
    """Decorator to add returnType, argTypes and argNames to a function"""
    def add_types( function ):
        """Adds the given metadata to the function, introspects var names from declaration"""
        function.resultType = resultType
        function.argTypes = argTypes 
        function.argNames = function.func_code.co_varnames
        return function 
    return add_types

def unpack_constants( constants, namespace ):
    """Create constants and add to the namespace"""
    from OpenGL.constant import Constant
    for line in constants.splitlines():
        if line and line.split():
            name,value = line.split()
            namespace[name] = Constant( name, int(value,16) )

def createFunction( function, dll,extension,deprecated ):
    """Allows the more compact declaration format to use the old-style constructor"""
    return createExtensionFunction(
        function.__name__,
        dll,
        resultType = function.resultType,
        argTypes = function.argTypes,
        doc = None, argNames = function.argNames,
        extension = extension,
        deprecated = deprecated,
        module = function.__module__,
    )
