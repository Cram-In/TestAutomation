from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    packages=find_packages("play"),
    package_dir={"": "play"},
)