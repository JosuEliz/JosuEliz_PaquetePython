from setuptools import setup

setup(
   name='PaqueteJosuEliz',
   version='1.0.0',
   author='Josu Elizburu',
   author_email='jelizburu001@ikasle.ehu.eus',
   packages=['PaqueteJosuEliz', 'PaqueteJosuEliz.test'],
   url='https://github.com/JosuEliz/JosuEliz_PaquetePython',
   license='LICENSE.txt',
   description='Este paquete es un paquete para complementar la entrega basica de Software Matematico y Estadistico',
   long_description=open('README.txt').read(),
   tests_require=['pytest'],
   install_requires=[
      "numpy >=1.23.3"
   ],
)
