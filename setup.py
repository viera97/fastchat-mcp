from setuptools import setup, find_packages

setup(
    name="mcp-client-py",
    version="1.0.0",
    packages=find_packages(),
    author="Tu Nombre",
    author_email="rb58853@gmail.com",
    description="Descripción breve de mi proyecto",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rb58853/python-mcp-client",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
