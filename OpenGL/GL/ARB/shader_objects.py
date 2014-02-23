'''OpenGL extension ARB.shader_objects

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_objects to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_objects.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.shader_objects import *
from OpenGL.raw.GL.ARB.shader_objects import _EXTENSION_NAME

def glInitShaderObjectsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
import OpenGL
from OpenGL._bytes import bytes, _NULL_8_BYTE, as_8_bit
from OpenGL.raw.GL import _errors
from OpenGL.lazywrapper import lazy as _lazy
from OpenGL import converters, error
GL_INFO_LOG_LENGTH_ARB = constant.Constant( 'GL_INFO_LOG_LENGTH_ARB', 0x8B84 )

glShaderSourceARB = platform.createExtensionFunction(
    'glShaderSourceARB', dll=platform.PLATFORM.GL,
    resultType=None,
    argTypes=(_types.GLhandleARB, _types.GLsizei, ctypes.POINTER(ctypes.c_char_p), arrays.GLintArray,),
    doc = 'glShaderSourceARB( GLhandleARB(shaderObj), [bytes(string),...] ) -> None',
    argNames = ('shaderObj', 'count', 'string', 'length',),
    extension = _EXTENSION_NAME,
)
conv = converters.StringLengths( name='string' )
glShaderSourceARB = wrapper.wrapper(
    glShaderSourceARB
).setPyConverter(
    'count' # number of strings
).setPyConverter(
    'length' # lengths of strings
).setPyConverter(
    'string', conv.stringArray
).setCResolver(
    'string', conv.stringArrayForC,
).setCConverter(
    'length', conv,
).setCConverter(
    'count', conv.totalCount,
)
try:
    del conv
except NameError as err:
    pass

for size in (1,2,3,4):
    for format,arrayType in (
        ('f',arrays.GLfloatArray),
        ('i',arrays.GLintArray),
    ):
        name = 'glUniform%(size)s%(format)svARB'%globals()
        globals()[name] = arrays.setInputArraySizeType(
            globals()[name],
            None, # don't want to enforce size...
            arrayType,
            'value',
        )
        try:
            del format, arrayType
        except NameError as err:
            pass
    try:
        del size
    except NameError as err:
        pass

@_lazy( glGetObjectParameterivARB )
def glGetObjectParameterivARB( baseOperation, shader, pname ):
    """Retrieve the integer parameter for the given shader"""
    status = arrays.GLintArray.zeros( (1,))
    status[0] = 1
    baseOperation(
        shader, pname, status
    )
    return status[0]

@_lazy( glGetObjectParameterfvARB )
def glGetObjectParameterfvARB( baseOperation, shader, pname ):
    """Retrieve the float parameter for the given shader"""
    status = arrays.GLfloatArray.zeros( (1,))
    status[0] = 1.0
    baseOperation(shader, pname,status)
    return status[0]

def _afterCheck( key ):
    """Generate an error-checking function for compilation operations"""
    def GLSLCheckError(
        result,
        baseOperation=None,
        cArguments=None,
        *args
    ):
        result = _errors._error_checker.glCheckError( result, baseOperation, cArguments, *args )
        status = glGetObjectParameterivARB(
            cArguments[0], key
        )
        if not status:
            raise error.GLError(
                result = result,
                baseOperation = baseOperation,
                cArguments = cArguments,
                description= glGetInfoLogARB( cArguments[0] )
            )
        return result
    return GLSLCheckError

if OpenGL.ERROR_CHECKING:
    glCompileShaderARB.errcheck = _afterCheck( GL_OBJECT_COMPILE_STATUS_ARB )
if OpenGL.ERROR_CHECKING:
    glLinkProgramARB.errcheck = _afterCheck( GL_OBJECT_LINK_STATUS_ARB )
## Not sure why, but these give invalid operation :(
##if glValidateProgramARB and OpenGL.ERROR_CHECKING:
##	glValidateProgramARB.errcheck = _afterCheck( GL_OBJECT_VALIDATE_STATUS_ARB )

@_lazy( glGetInfoLogARB )
def glGetInfoLogARB( baseOperation, obj ):
    """Retrieve the program/shader's error messages as a Python string

    returns string which is '' if no message
    """
    length = int(glGetObjectParameterivARB(obj, GL_INFO_LOG_LENGTH_ARB))
    if length > 0:
        log = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, log)
        return log.value.strip(_NULL_8_BYTE) # null-termination
    return ''

@_lazy( glGetAttachedObjectsARB )
def glGetAttachedObjectsARB( baseOperation, obj ):
    """Retrieve the attached objects as an array of GLhandleARB instances"""
    length= glGetObjectParameterivARB( obj, GL_OBJECT_ATTACHED_OBJECTS_ARB )
    if length > 0:
        storage = arrays.GLuintArray.zeros( (length,))
        baseOperation( obj, length, None, storage )
        return storage
    return arrays.GLuintArray.zeros( (0,))

@_lazy( glGetShaderSourceARB )
def glGetShaderSourceARB( baseOperation, obj ):
    """Retrieve the program/shader's source code as a Python string

    returns string which is '' if no source code
    """
    length = int(glGetObjectParameterivARB(obj, GL_OBJECT_SHADER_SOURCE_LENGTH_ARB))
    if length > 0:
        source = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, source)
        return source.value.strip(_NULL_8_BYTE) # null-termination
    return ''

@_lazy( glGetActiveUniformARB )
def glGetActiveUniformARB(baseOperation, program, index):
    """Retrieve the name, size and type of the uniform of the index in the program"""
    max_index = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_UNIFORMS_ARB ))
    length = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB))
    if index < max_index and index >= 0:
        if length > 0:
            name = ctypes.create_string_buffer(length)
            namelen = arrays.GLsizeiArray.zeros( (1,))
            size = arrays.GLintArray.zeros( (1,))
            gl_type = arrays.GLenumArray.zeros( (1,))
            baseOperation(program, index, length,namelen,size, gl_type, name)
            return name.value[:int(namelen[0])], size[0], gl_type[0]
        raise ValueError( """No currently specified uniform names""" )
    raise IndexError('Index %s out of range 0 to %i' % (index, max_index - 1, ))

@_lazy( glGetUniformLocationARB )
def glGetUniformLocationARB( baseOperation, program, name ):
    """Check that name is a string with a null byte at the end of it"""
    if not name:
        raise ValueError( """Non-null name required""" )
    name = as_8_bit( name )
    if name[-1] != _NULL_8_BYTE:
        name = name + _NULL_8_BYTE
    return baseOperation( program, name )
