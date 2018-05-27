from setuptools import setup, find_packages

setup(
    name='ZTD library',
    version='0.1',
    packages=find_packages(exclude=['calculations*', 'FileManager*', 'StructureFile*']),
    description='Library to calculate ZTD',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://mozog226125@git.e-science.pl/mozog226125/libraryZTD.git',
    author='Mateusz Ozog',
    author_email='226125@student.pwr.edu.pl'
)
