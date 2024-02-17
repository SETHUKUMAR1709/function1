from setuptools import find_packages, setup

setup(
    name="firstlib",
    version="0.0.10",
    description="simple lib",
    package_dir={},
    packages=find_packages(),
    url="https://github.com/SETHUKUMAR1709/integrated/tree/main/firstlib",
    author="GGEZ",
    author_email="sethukumars774@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={},
    python_requires=">=3.11",
)