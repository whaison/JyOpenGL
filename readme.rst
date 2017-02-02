JyOpenGL

JyOpenGLプロジェクトは、Jython上で動作するように調整されたPyOpenGLのフォークです。 JyOpenGLはポートではないことに注意してください。この調整は、この執筆時点のように、CPythonとの互換性には触れていないからです。したがって、JyOpenGLはJythonとCPythonで同時に実行可能です。しかし、CPythonで明示的にテストされていません。 JyOpenGLは別のプロジェクトとして作成されました.JythonとJavaの統合、AWTベースのレンダリングフロントエンド、Jythonスタイルのデプロイメント構造を追加する予定です。プリコンパイルされたJyOpenGLライブラリを含むJython準拠のjarファイルを作成するビルドスクリプト。

JythonでJyOpenGLを使用するには、十分に完全なctypes実装が必要です。現在、Jythonの組み込みJFFIベースのctypes実装では、この目的では十分ではありません。

現時点で有効な方法は、JyNI（www.jyni.org）をネイティブのctypeで使用することです。 JyNIは他のPOSIXプラットフォームもサポートしていますが、説明された設定はLinux（LMDE2,64ビット）でしかテストされていません。この設定の詳細な設定手順は、近い将来このセクションに追加されます。

以下のオリジナルのPyOpenGL-readmeを探します：

PyOpenGLとPyOpenGL_accelerate

PyOpenGLは通常、標準pipを使用してPyPI経由で配布されます：

$ pip install PyOpenGL PyOpenGL_accelerate
このリポジトリは、ブランチング/クローニングとsetup.pyの実行によってインストールできます：

$ cd pyopengl
$ python setup.py develop
$ cd加速
$ python setup.py develop
PyOpenGL_accelerateをコンパイルするには、機能するPython拡張コンパイル環境が必要であることに注意してください。

PyOpenGLを学ぶ

PyOpenGLを初めてお使いの方は、OpenGLContextチュートリアルページから始めたいと思うでしょう。これらのチュートリアルではOpenGLContext（シーングラフエンジン全体、VRML97パーサー、たくさんのデモなどの大きなラッパー）が必要です：

$ pip2.7 install "OpenGLContext-full == 3.1.1
または（チュートリアルのソースを含む）それを複製するには：

$ bzrブランチlp：openglcontext
ドキュメントページは、PyOpenGL呼び出しのパラメータとセマンティクスを調べるのに便利です。

テストの実行

PyOpenGLテストスイートを実行するには、PygameとNumpyホイールをPython 2.7,3.4、および3.5とともにあらかじめ作成しておく必要があります。テストスイート用のホイールは、ルートチェックアウトと同じレベルの "wheelhouse"というディレクトリに格納する必要があります。

Ubuntuで車輪を作るには：

$ hgクローンhttps://bitbucket.org/pygame/pygame
$ apt-get build-dep pygame python-numpy
$ pip2.7 wheel / pygame numpy
$ pip3.4 wheel / pygame numpy
$ pip3.5 wheel / pygame numpy
あなたがpyopenglをチェックアウトしたのと同じディレクトリでそれを行うと、pyopengl toxスイートが予期しているディレクトリにすべてのホイールが置かれます。

toxを実行するには、明らかにtoxがインストールされている必要があります。次のようになります。

$ tox
その結果、多くのテストがPythonバージョンの環境のマトリックスで実行されていました。

2.7
3.5
3.4
アクセラレーションモジュールを使用する場合と使用しない場合、および環境にnumpyがインストールされている場合とインストールされていない場合をテストします。
JyOpenGL JyOpenGL purojekuto wa, Jython-jō de dōsa suru yō ni chōsei sa reta PyOpenGL no fōkudesu. 




JyOpenGL
========

The JyOpenGL project is a fork of PyOpenGL containing adjustments that allow it to
run on Jython. Note that JyOpenGL is not a port, since the adjustments are so
minimal that - as of this writing - they don't touch CPython compatibility.
So JyOpenGL is workable on Jython and CPython at the same time. However it is not
explicitly tested on CPython.
Still JyOpenGL was created to be a separate project, because we will add additional
Jython- and Java-intergration features, an AWT-based rendering frontend and
Jython-style deployment structure, e.g. a build-script to create a Jython-compliant
jar-file containing a precompiled JyOpenGL library.

To use JyOpenGL on Jython, a sufficiently complete ctypes implementation for Jython is
required. As of this writing Jython's builtin JFFI-based ctypes implementation is
*not* sufficient for this purpose.

Currently the only known workable way is to use JyNI (www.jyni.org) with native ctypes.
While JyNI also supports other posix platforms, the described setup was only tested
on Linux (LMDE2, 64 bit) yet.
Detailed setup instructions for this configuration will be appended to this section
in near future.


Find the original PyOpenGL-readme below:
----------------------------------------


PyOpenGL and PyOpenGL_accelerate
=================================

PyOpenGL is normally distributed via PyPI using standard pip::

    $ pip install PyOpenGL PyOpenGL_accelerate

You can install this repository by branching/cloning and running
setup.py::

    $ cd pyopengl
    $ python setup.py develop
    $ cd accelerate
    $ python setup.py develop

Note that to compile PyOpenGL_accelerate you will need to have 
a functioning Python extension-compiling environment.

Learning PyOpenGL
-----------------

If you are new to PyOpenGL, you likely want to start with the OpenGLContext `tutorial page`_.
Those tutorials require OpenGLContext, (which is a big wrapper including a whole
scenegraph engine, VRML97 parser, lots of demos, etc) you can install that with::

    $ pip2.7 install "OpenGLContext-full==3.1.1

Or you can clone it (including the tutorial sources) with::

    $ bzr branch lp:openglcontext
    
The `documentation pages`_ are useful for looking up the parameters and semantics of 
PyOpenGL calls.

.. _`tutorial page`: http://pyopengl.sourceforge.net/context/tutorials/index.html
.. _`documentation pages`: http://pyopengl.sourceforge.net/documentation/


Running Tests
--------------

You can run the PyOpenGL test suite only if you have prebuilt Pygame and 
Numpy wheels, along with Python 2.7, 3.4 and 3.5. The 
wheels for the test suite to use should be stored in a directory
called "wheelhouse" at the same level as the root checkout here.

To build the wheels on Ubuntu::

    $ hg clone https://bitbucket.org/pygame/pygame
    $ apt-get build-dep pygame python-numpy
    $ pip2.7 wheel ./pygame numpy
    $ pip3.4 wheel ./pygame numpy
    $ pip3.5 wheel ./pygame numpy

if you do that in the same directory where you checked out pyopengl
you will have all of your wheels in the directory the pyopengl 
tox suite is expecting.

You'll obviously need `tox` installed to run tox, which looks
like this::

    $ tox

The result being a lot of tests being run in a matrix of environments,
with Python versions:

    * 2.7
    * 3.5
    * 3.4

Where we test with and without the accelerate module and with and 
without numpy installed in the environment.

