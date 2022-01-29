import setuptools

from tgfilestream import __version__

try:
    long_desc = open("README.md").read()
except IOError:
    long_desc = "Failed to read README.md"

setuptools.setup(
    name="tgfilestream",
    version="0.1.0",
    version=__version__,
    url="https://mau.dev/tulir/tgfilestream",

    author="Tulir Asokan",
@@ -40,6 +42,6 @@
    ],
    entry_points="""
        [console_scripts]
        tgfilestream=tgfilestream:main
        tgfilestream=tgfilestream.__main__:main
    """,
)
