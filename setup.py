import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='xspfclean',
    version='0.2',
    scripts=['xspfclean'] ,
    author="Ibrahim E.Gad",
    author_email="eibrahim995@yandex.com",
    description="Xspf playlist files cleaner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eibrahim995/xspfcleaner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Common Public License",
        "Operating System :: OS Independent",
    ],
)
