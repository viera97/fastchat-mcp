from setuptools import setup, find_packages
from pathlib import Path
import os

try:
    HERE = Path(__file__).parent.resolve()
    README = HERE / "readme.md"

    with open(README, encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "readme.md no encontrado. Por favor, revise la documentación."
except Exception as e:
    long_description = f"Error leyendo readme.md: {str(e)}"

setup(
    name="mcp-client",
    version="1.0.0",
    packages=find_packages(),
    author="Raúl Beltrán Gómez",
    author_email="rb58853@gmail.com",
    description="Python client, based on `fastmcp`, for connecting to MCP servers through multiple protocols, specifically designed to work with integrated language models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rb58853/python-mcp-client",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
