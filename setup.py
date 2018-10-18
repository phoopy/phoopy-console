from setuptools import setup
import phoopy.console

long_description = open('README.rst', 'r').read()

setup(
    name='phoopy-console',
    version=phoopy.console.__version__,
    packages=['phoopy', 'phoopy.console', 'phoopy.console.helper'],
    setup_requires=['wheel'],
    install_requires=['phoopy-kernel>=1.1.0,<1.2.0','cleo==0.6.8'],
    description="Console library for phoopy framework",
    long_description=long_description,
    url='https://github.com/phoopy/phoopy-console',
    author='Phoopy',
    author_email='reisraff@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
