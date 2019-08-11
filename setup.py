from setuptools import setup, find_packages

setup(name='caged_nerd',
      version='1.0',
      description='A nerdy practice tool for guitarists',
      classifiers=[
              'Development Status :: 4 - Beta',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3.7',
              'Topic :: Education'],
      install_requires=['pytest'],
      author='Lachlan McLachlan',
      author_email='lachlan.mclachlan@outlook.com',
      url='https://github.com/LachlanMcLachlan/caged_nerd',
      license='MIT',
      packages=find_packages(where=r'./src'),
      zip_safe=False)

