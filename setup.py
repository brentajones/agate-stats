#!/usr/bin/env python

from setuptools import setup

install_requires = [
    'agate>=1.0.0'
]

setup(
    name='agate-stats',
    version='0.3.0',
    description='agate-stats adds additional statistical methods to agate.',
    long_description=open('README').read(),
    author='Christopher Groskopf',
    author_email='chrisgroskopf@gmail.com',
    url='http://agate-stats.readthedocs.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'agatestats'
    ],
    install_requires=install_requires
)
