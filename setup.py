"""setup.py."""
from setuptools import find_packages
from setuptools import setup

setup(
    name="validatedoc",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    author="Matthew Bentley",
    author_email="matthew@bentley.link",
    description="Do some doc string validateion",
    entry_points={
        'console_scripts': [
            'validatedoc = validatedoc.validatadoc:main',
        ],
    },
    install_requires=[],
)
