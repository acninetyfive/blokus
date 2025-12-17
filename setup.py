from setuptools import setup, find_packages

setup(
    name='blokus',
    install_requires=[
        'pygame',
        'numpy',
        'scipy',
    ],
    packages=find_packages(),
)
