from setuptools import setup


# def readme():
#     with open('README.rst') as f:
#         return f.read()

setup(name='django-email',
      version='0.1.1',
      description='Django Emails made easy',
      # long_description=readme(),
      url='https://github.com/swappsco/django-email',
      author='Andres Gonzalez',
      author_email='andresgz@gmail.com',
      license='MIT',
      packages=['django_email'],
      include_package_data=True,
      install_requires=[
          'django',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License', # example license
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      zip_safe=False)
