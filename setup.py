# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="pythaitts",
    version="0.1",
    description="TTS for Thai Language",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/wannaphongcom/pythaitts",
    packages=find_packages(),
    python_requires=">=3.4",
    #package_data={},
    include_package_data=True,
    #install_requires=requirements,
    #extras_require=extras,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="TTS",
    classifiers=[
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Text Processing :: Linguistic",
    ]
)
