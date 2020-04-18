import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="AirzoneCloud",
    version="0.1.0",
    description="Access to AirzoneCloud API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/max13fr/airzonecloud",
    author="max13fr",
    author_email="max13fr@yozo.fr",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["AirzoneCloud"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={},
)
