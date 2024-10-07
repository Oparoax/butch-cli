from setuptools import setup, find_packages

setup(
    name='butch_OS',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_start=butch_OS.main:main',
        ]
    }
)
