'''OpenGL extension OES.stencil4

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.stencil4 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/stencil4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES1 import _types
from OpenGL.raw.GLES1.OES.stencil4 import *
from OpenGL.raw.GLES1.OES.stencil4 import _EXTENSION_NAME

def glInitStencil4OES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION