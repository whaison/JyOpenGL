'''OpenGL extension OES.read_format

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_OES_read_format'
_DEPRECATED = False
GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = constant.Constant( 'GL_IMPLEMENTATION_COLOR_READ_TYPE_OES', 0x8B9A )
GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = constant.Constant( 'GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES', 0x8B9B )


def glInitReadFormatOES():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )