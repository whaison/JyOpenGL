'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_APPLE_texture_max_level'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_APPLE_texture_max_level',error_checker=_errors._error_checker)
GL_TEXTURE_MAX_LEVEL_APPLE=_C('GL_TEXTURE_MAX_LEVEL_APPLE',0x813D)

