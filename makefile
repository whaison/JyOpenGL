#
# makefile for JyNI
#
# Author: Stefan Richthofer
#

JAVA = java
OUTPUTDIR = ./build

# Adjust the following line to point to Jython 2.7
JYTHON = ./jython.jar
#for instance, if you extracted it to your home folder:
#JYTHON = /home/your_name/jython.jar

# Adjust the Java path below to match your system, if not yet appropriate
JAVA_HOME = /usr/lib/jvm/default-java
#The symlink "default-java" does not exist on every system. If gnumake tells you that the header
#jni.h is missing, please adjust JAVA_HOME appropriately. Example for Java 7, 64 bit:
#JAVA_HOME = /usr/lib/jvm/java-7-openjdk-amd64
PLATFORM = linux

JYOPENGLBIN = ./build_tmp

all: JyOpenGL
	@echo ''
	@echo 'Build successful.'

$(OUTPUTDIR):
	mkdir $(OUTPUTDIR)

$(JYOPENGLBIN):
	mkdir $(JYOPENGLBIN)

$(JYOPENGLBIN)/Lib: $(JYOPENGLBIN)
	cp -r OpenGL $(JYOPENGLBIN)
	$(JAVA) -cp $(JYTHON) org.python.util.jython -c "import compileall; compileall.compile_dir('$(JYOPENGLBIN)')"
	cp license.txt $(JYOPENGLBIN)

$(JYTHON):
	@echo ''
	@echo '------------------------------------------------'
	@echo 'Fatal error: Could not find jython.jar.'
	@echo 'Either put jython.jar into JyOpenGL base folder,'
	@echo 'or adjust the JYTHON-variable at the top of'
	@echo 'makefile to point to your installed jython.jar.'
	@echo 'Be sure to use Jython 2.7.1 or newer.'
	@echo '------------------------------------------------'
	@echo ''
	@false

JyOpenGL: $(OUTPUTDIR) $(JYTHON) $(JYOPENGLBIN)/Lib
	cp license.txt $(JYOPENGLBIN)
	jar cvf $(OUTPUTDIR)/JyOpenGL.jar -C $(JYOPENGLBIN) .

clean:
	rm -rf $(JYOPENGLBIN)

.PHONY: JyOpenGL clean all

