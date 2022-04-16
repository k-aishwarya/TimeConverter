import setuptools
setuptools.setup(
     name='timeConverter',  
     version='3.2',
     scripts=['TimeConverter'] ,
     author="Kumari Aishwarya",
     author_email="k.aishwarya15@gmail.com",
     description="A GUI tool to convert time across all time zones. To use this tool, "
                 "just type 'timeConverter' on your terminal.",
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