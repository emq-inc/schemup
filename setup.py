from setuptools import setup, find_packages

setup(name="schemup",
      version="1.0",

      description="Database-agnostic schema upgrade tools",
      author="Brendon Hogger",
      author_email="brendonh@gmail.com",
      url="https://github.com/brendonh/schemup",
      long_description=open('README.md').read(),

      packages=find_packages(),

      install_requires=[
            "six==1.15.0",
            "PyYAML==5.4.1",
            "psycopg2-binary==2.8.6"
      ],

      package_data={
      },

      )
