from setuptools import find_packages, setup

setup(
    name="firstlib",
    version="0.0.10",
    description="simple lib",
    package_dir={},
    packages=find_packages(),
    url="https://github.com/ArjanCodes/2023-package",
    author="ArjanCodes",
    author_email="arjan@arjancodes.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)