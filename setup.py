
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'TomTom API library'
LONG_DESCRIPTION = 'A package to simplify the usage of the TomTom API'

# Setting up
setup(
    name="tomtombrumbrum",
    version=VERSION,
    author="Gabriele Trevisan",
    author_email="<gabriele.3vi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['json', 'requests'],
    keywords=['python', 'tomtom', 'api', 'drive'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)