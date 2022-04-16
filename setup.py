import setuptools
setuptools.setup(
     name='timeConverter',  
     version='3.1',
     scripts=['TimeConverter'] ,
     author="Kumari Aishwarya",
     author_email="k.aishwarya15@gmail.com",
     description="A tool to convert time across time zones",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
          'pytz'
      ],
 )