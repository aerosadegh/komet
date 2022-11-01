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
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
