'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_KHR_create_context'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_KHR_create_context',error_checker=_errors._error_checker)
EGL_CONTEXT_FLAGS_KHR=_C('EGL_CONTEXT_FLAGS_KHR',0x30FC)
EGL_CONTEXT_MAJOR_VERSION_KHR=_C('EGL_CONTEXT_MAJOR_VERSION_KHR',0x3098)
EGL_CONTEXT_MINOR_VERSION_KHR=_C('EGL_CONTEXT_MINOR_VERSION_KHR',0x30FB)
EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT_KHR=_C('EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT_KHR',0x00000002)
EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT_KHR=_C('EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT_KHR',0x00000001)
EGL_CONTEXT_OPENGL_DEBUG_BIT_KHR=_C('EGL_CONTEXT_OPENGL_DEBUG_BIT_KHR',0x00000001)
EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE_BIT_KHR=_C('EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE_BIT_KHR',0x00000002)
EGL_CONTEXT_OPENGL_PROFILE_MASK_KHR=_C('EGL_CONTEXT_OPENGL_PROFILE_MASK_KHR',0x30FD)
EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_KHR=_C('EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_KHR',0x31BD)
EGL_CONTEXT_OPENGL_ROBUST_ACCESS_BIT_KHR=_C('EGL_CONTEXT_OPENGL_ROBUST_ACCESS_BIT_KHR',0x00000004)
EGL_LOSE_CONTEXT_ON_RESET_KHR=_C('EGL_LOSE_CONTEXT_ON_RESET_KHR',0x31BF)
EGL_NO_RESET_NOTIFICATION_KHR=_C('EGL_NO_RESET_NOTIFICATION_KHR',0x31BE)
EGL_OPENGL_ES3_BIT_KHR=_C('EGL_OPENGL_ES3_BIT_KHR',0x00000040)

