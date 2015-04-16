from setuptools import setup
import platform

setup(name='syscertifi',
      author="Seppo Yli-Olli",
      author_email="seppo.yli-olli+pypi@iki.fi",
      description="Make requests use system certificate stores",
      py_modules=["certifi"],
      extras_require={":sys_platform=='win32'": ["wincertstore"]},
      version="0.1"
      )
