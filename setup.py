from setuptools import setup, find_packages
from audioplayer import __name__, __package__, __version__

__author__ = "Marcos Brusso"
__author_email__="mjbrusso@gmail.com"
__license__ ="MIT License"
__desc__ = "audioplayer is a cross platform Python 3 module for playing sounds (mp3, wav, ...)"
__python_requires__ = ">=3"
__keywords__ = [
    "sound",
    __name__,
    "music",
    "player",
    "game",
    "games",
    "mp3",
    "wav",
    "audio"
]
__url__ = "https://github.com/mjbrusso/audioplayer"

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Topic :: Multimedia",
    "Topic :: Multimedia :: Sound/Audio",
    "Topic :: Multimedia :: Sound/Audio :: Players",
    "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
    "Intended Audience :: Developers"
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
]

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__desc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=__license__,
    keywords=__keywords__,
    url=__url__,
    packages=find_packages(),
    classifiers=__classifiers__,
    install_requires=[],
    # extras_require=[],
    python_requires=__python_requires__,
)
