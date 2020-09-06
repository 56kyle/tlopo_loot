import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tlopo_loot", # Replace with your own username
    version="0.0.1",
    author="Kyle Oliver",
    author_email="56kyleoliver@gmail.com",
    description="A tool for finding which enemies are most likely to drop a given item",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/56kyle/tlopo_loot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
