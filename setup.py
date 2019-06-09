# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="thaitts",
    version="0.2dev1",
    description="Open source thai text to speech engine.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/wannaphongcom/pythaitts",
    packages=find_packages(),
    python_requires=">=3.4",
    package_data={"pythaitts":["thai2ipa.txt"]},
    include_package_data=True,
    install_requires=["pythainlp>=2.0"],
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
