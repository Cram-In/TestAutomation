from setuptools import setup, find_packages

setup(
    name="converter",
    packages=find_packages("src"),
    package_dir={"": "src"},
)