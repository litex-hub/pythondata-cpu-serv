import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_cpu_serv import version_str

setuptools.setup(
    name="pythondata-cpu-serv",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="""\
Python module containing verilog files for serv cpu.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-cpu-serv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'cpu_serv': ['cpu_serv/verilog/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-cpu-serv/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-cpu-serv",
    },
)
