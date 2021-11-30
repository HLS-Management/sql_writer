import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sql_writer",
    version="0.0.1",
    author="HLS Management",
    description="package that spits out SQL so you dont have to write it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HLS-Management/sql_writer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)