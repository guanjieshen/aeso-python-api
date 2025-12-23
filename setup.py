"""Setup configuration for AESO Python API"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="aeso",
    version="0.2.0",
    author="Guanjie Shen",
    description="A Python wrapper for the Alberta Electric System Operator (AESO) API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guanjieshen/aeso-python-api",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    keywords="aeso alberta electricity api pool price energy market",
    project_urls={
        "Bug Reports": "https://github.com/guanjieshen/aeso-python-api/issues",
        "Source": "https://github.com/guanjieshen/aeso-python-api",
        "Documentation": "https://github.com/guanjieshen/aeso-python-api#readme",
    },
)
