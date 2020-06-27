from distutils.core import setup
setup(
  name = 'calc',         
  packages = ['calc'],   
  version = '1.0',      
  license='MIT',        
  description = 'This package returns calctiplication of two integers.',   
  url = 'https://github.com/majorx234/python-calc',   
  download_url = 'https://github.com/YugantM/python-calc.git',  
  install_requires=[
      'add',
	    'mul'
    ],  
  scripts=['scripts/calc'],    
  keywords = ['add','multiplication', 'calculation'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
