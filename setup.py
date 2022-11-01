from setuptools import find_packages, setup

version = "0.1.0"
DESCRIPTION = "A print package"
LONG_DESCRIPTION = "A simple class for print python objects with tails."

setup(
    name="comet",
    version=version,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Sadegh Yazdani",
    author_email="m.s.yazdani85@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords="conversion",
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
)
