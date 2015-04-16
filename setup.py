from setuptools import setup
import platform

setup(name='syscertifi',
      description="Make requests use system certificate stores",
      py_modules=["certifi"],
      extras_require={":sys_platform=='win32'": ["wincertstore"]},
      version="0.1"
      )
