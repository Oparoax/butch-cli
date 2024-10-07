from setuptools import setup

setup(
    name='butch_OS',
    version='1.0',
    packages=find_packages(),
    scripts=['butch_OS/main.py', 'butch_OS/module/funky_print.py', 'butch_OS/module/file_importer.py', 'butch_OS/module/progress.py']
)

