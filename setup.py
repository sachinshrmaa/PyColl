import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
   
    name="pycoll",
    version="0.0.2",
    author="Sachin Sharma",
    author_email="contact@sachinshrmaa.com",
    description="Find Area of Square, Rectangle, Triangle and Parallelogram ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sachinshrmaa/pycoll",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
