from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="my_name",
    author_email="peacchaves@gmail.com",
    description="Usando transformada de fourier para análise de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url=""
    packages=find_packages(),
    install_requires=('requirements.txt'),
    python_requires='>=3.8',
)