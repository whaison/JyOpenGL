'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_draw_buffers'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_draw_buffers',error_checker=_errors._error_checker)
GL_COLOR_ATTACHMENT0_NV=_C('GL_COLOR_ATTACHMENT0_NV',0x8CE0)
GL_COLOR_ATTACHMENT10_NV=_C('GL_COLOR_ATTACHMENT10_NV',0x8CEA)
GL_COLOR_ATTACHMENT11_NV=_C('GL_COLOR_ATTACHMENT11_NV',0x8CEB)
GL_COLOR_ATTACHMENT12_NV=_C('GL_COLOR_ATTACHMENT12_NV',0x8CEC)
GL_COLOR_ATTACHMENT13_NV=_C('GL_COLOR_ATTACHMENT13_NV',0x8CED)
GL_COLOR_ATTACHMENT14_NV=_C('GL_COLOR_ATTACHMENT14_NV',0x8CEE)
GL_COLOR_ATTACHMENT15_NV=_C('GL_COLOR_ATTACHMENT15_NV',0x8CEF)
GL_COLOR_ATTACHMENT1_NV=_C('GL_COLOR_ATTACHMENT1_NV',0x8CE1)
GL_COLOR_ATTACHMENT2_NV=_C('GL_COLOR_ATTACHMENT2_NV',0x8CE2)
GL_COLOR_ATTACHMENT3_NV=_C('GL_COLOR_ATTACHMENT3_NV',0x8CE3)
GL_COLOR_ATTACHMENT4_NV=_C('GL_COLOR_ATTACHMENT4_NV',0x8CE4)
GL_COLOR_ATTACHMENT5_NV=_C('GL_COLOR_ATTACHMENT5_NV',0x8CE5)
GL_COLOR_ATTACHMENT6_NV=_C('GL_COLOR_ATTACHMENT6_NV',0x8CE6)
GL_COLOR_ATTACHMENT7_NV=_C('GL_COLOR_ATTACHMENT7_NV',0x8CE7)
GL_COLOR_ATTACHMENT8_NV=_C('GL_COLOR_ATTACHMENT8_NV',0x8CE8)
GL_COLOR_ATTACHMENT9_NV=_C('GL_COLOR_ATTACHMENT9_NV',0x8CE9)
GL_DRAW_BUFFER0_NV=_C('GL_DRAW_BUFFER0_NV',0x8825)
GL_DRAW_BUFFER10_NV=_C('GL_DRAW_BUFFER10_NV',0x882F)
GL_DRAW_BUFFER11_NV=_C('GL_DRAW_BUFFER11_NV',0x8830)
GL_DRAW_BUFFER12_NV=_C('GL_DRAW_BUFFER12_NV',0x8831)
GL_DRAW_BUFFER13_NV=_C('GL_DRAW_BUFFER13_NV',0x8832)
GL_DRAW_BUFFER14_NV=_C('GL_DRAW_BUFFER14_NV',0x8833)
GL_DRAW_BUFFER15_NV=_C('GL_DRAW_BUFFER15_NV',0x8834)
GL_DRAW_BUFFER1_NV=_C('GL_DRAW_BUFFER1_NV',0x8826)
GL_DRAW_BUFFER2_NV=_C('GL_DRAW_BUFFER2_NV',0x8827)
GL_DRAW_BUFFER3_NV=_C('GL_DRAW_BUFFER3_NV',0x8828)
GL_DRAW_BUFFER4_NV=_C('GL_DRAW_BUFFER4_NV',0x8829)
GL_DRAW_BUFFER5_NV=_C('GL_DRAW_BUFFER5_NV',0x882A)
GL_DRAW_BUFFER6_NV=_C('GL_DRAW_BUFFER6_NV',0x882B)
GL_DRAW_BUFFER7_NV=_C('GL_DRAW_BUFFER7_NV',0x882C)
GL_DRAW_BUFFER8_NV=_C('GL_DRAW_BUFFER8_NV',0x882D)
GL_DRAW_BUFFER9_NV=_C('GL_DRAW_BUFFER9_NV',0x882E)
GL_MAX_DRAW_BUFFERS_NV=_C('GL_MAX_DRAW_BUFFERS_NV',0x8824)
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDrawBuffersNV(n,bufs):pass
