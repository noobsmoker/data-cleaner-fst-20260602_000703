from setuptools import setup, find_packages

setup(
    name="data-cleaner-fst-20260602_000703",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'data=data:main',
        ],
    },
)
