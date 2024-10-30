from setuptools import setup, find_packages

setup(
    name='osiris-function-library',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest==6.2.5',
        'unittest2',
        'mock'
    ],
    python_requires='==3.9',
)
