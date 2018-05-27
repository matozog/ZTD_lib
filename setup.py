from setuptools import setup, find_packages

setup(
    name='libraryZTD',
    version='0.1',
    packages=find_packages(exclude=['calculations*', 'FileManager*', 'StructureFile*']),
    description='Library to calculate ZTD',
    long_description=open('README.md').read(),
    url='https://github.com/matozog/libraryZTD.git',
    author='Mateusz Ozog',
    author_email='226125@student.pwr.edu.pl'
)
