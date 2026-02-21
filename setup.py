from setuptools import setup, find_packages

setup(
    name="terminai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "google-generativeai",
        "python-dotenv",
        "pwinput",
    ],

    entry_points={
        "console_scripts": [
            "terminai=terminai.cli:main",
        ],
    },
)
