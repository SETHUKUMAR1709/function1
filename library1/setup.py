import setuptools
setuptools.setup(
    name = "sethukumar",
    version= "0.0.1",
    description= "my first library",
    long_description= "This is my first library",
    author="sethukumar moorthy",
    packages= setuptools.find_packages(),
    url="https://github.com/SETHUKUMAR1709/integrated/tree/main/library1",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
    install_requires=["pandas"],
)