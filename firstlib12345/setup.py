from setuptools import find_packages, setup

setup(
    include_package_data=True,
    name="firstlib12345",
    version="0.0.20",
    description="simple lib",
    packages=find_packages(),
    author="GGEZ",
    author_email="sethukumars774@gmail.com",
    url="https://github.com/SETHUKUMAR1709/integrated/tree/main/firstlib12345",
    long_description="Blah Blah",
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)