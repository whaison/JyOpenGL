'''OpenGL extension ARB.ES3_2_compatibility

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.ES3_2_compatibility to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/ES3_2_compatibility.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.ES3_2_compatibility import *
from OpenGL.raw.GL.ARB.ES3_2_compatibility import _EXTENSION_NAME

def glInitEs32CompatibilityARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION