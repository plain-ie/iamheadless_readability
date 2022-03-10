from distutils.core import setup

setup(

    # Application name:
    name="iamheadless_readability",

    # Version number (initial):
    version="0.0.1",
    
    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_readability"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    extras_require=[
        "Django==4.0.1",
        "nltk==3.7",
        "py-readability-metrics==1.4.5",
    ],

)
