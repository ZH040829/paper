from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ierft-v5",
    version="5.1",
    author="郑豪",
    author_email="20253001490@hainanu.edu.cn",
    description="IERFT V5 - 智能熵减场论数字生命元控制层",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZH040829/ierft-v5",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'ierft-v5=v5:main',
        ],
    },
)
