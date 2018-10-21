from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pySlipQt',
      version='0.1.0',
      description='A slipmap widget for PyQt5',
      long_description=readme(),
      url='http://github.com/rzzzwilson/pySlipQt',
      author='Ross Wilson',
      author_email='rzzzwilson@gmail.com',
      license='MIT',
      packages=['pySlipQt'],
      install_requires=['pyqt5', 'python'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3 :: Only'],
      keywords='python pyqt5 slipmap map',
      data_files=[('pySlipQt/examples', ['pySlipQt/examples/README.rst',
                                         'pySlipQt/examples/display_text.py',
                                         'pySlipQt/examples/layer_control.py',
                                         'pySlipQt/examples/make_gmt_tiles.py',
                                         'pySlipQt/examples/numofcpus.py',
                                         'pySlipQt/examples/pyslipqt_demo.py',
                                         'pySlipQt/examples/tkinter_error.py',
                                         'pySlipQt/examples/utils.py',
                                         'pySlipQt/examples/test_assumptions.py',
                                         'pySlipQt/examples/test_display_text.py',
                                         'pySlipQt/examples/test_displayable_levels.py',
                                         'pySlipQt/examples/test_gmt_local_tiles.py',
                                         'pySlipQt/examples/test_gotoposition.py',
                                         'pySlipQt/examples/test_image_placement.py',
                                         'pySlipQt/examples/test_layer_control.py',
                                         'pySlipQt/examples/test_maprel_image.py',
                                         'pySlipQt/examples/test_maprel_polygon.py',
                                         'pySlipQt/examples/test_maprel_text.py',
                                         'pySlipQt/examples/test_multi_widget.py',
                                         'pySlipQt/examples/test_osm_tiles.py',
                                         'pySlipQt/examples/test_point_placement.py',
                                         'pySlipQt/examples/test_polygon_placement.py',
                                         'pySlipQt/examples/test_polyline_placement.py',
                                         'pySlipQt/examples/test_text_placement.py',
                                         'pySlipQt/examples/test_viewrel_image.py',
                                         'pySlipQt/examples/test_viewrel_point.py',
                                         'pySlipQt/examples/test_viewrel_polygon.py',
                                         'pySlipQt/examples/test_viewrel_text.py', 
                                        ]),
                  ('pySlipQt/examples/graphics', ['pySlipQt/examples/graphics/Qt_logo.png',
                                         'pySlipQt/examples/graphics/arrow_down.png',
                                         'pySlipQt/examples/graphics/arrow_left.png',
                                         'pySlipQt/examples/graphics/arrow_leftdown.png',
                                         'pySlipQt/examples/graphics/arrow_leftup.png',
                                         'pySlipQt/examples/graphics/arrow_right.png',
                                         'pySlipQt/examples/graphics/arrow_rightdown.png',
                                         'pySlipQt/examples/graphics/arrow_rightup.png',
                                         'pySlipQt/examples/graphics/arrow_up.png',
                                         'pySlipQt/examples/graphics/compass_rose.png',
                                         'pySlipQt/examples/graphics/error_tile.png',
                                         'pySlipQt/examples/graphics/img2py.py',
                                         'pySlipQt/examples/graphics/pending_image.png',
                                         'pySlipQt/examples/graphics/pyslip_demo_gmt.png',
                                         'pySlipQt/examples/graphics/pyslip_demo_osm.png',
                                         'pySlipQt/examples/graphics/pyslipqt_logo.png',
                                         'pySlipQt/examples/graphics/shipwreck.png',
                                        ]),
                 ],
      download_url='https://github.com/rzzzwilson/pySlipQt/releases/tag/0.1.0',
      include_package_data=True,
      zip_safe=False)



#from setuptools import setup, find_packages
#
#def readme():
#    with open('README.rst') as f:
#        return f.read()
#
#setup(name='pySlipQt',
#      version='0.1.0',
#      description='A slipmap widget for PyQt5',
#      long_description=readme(),
#      url='http://github.com/rzzzwilson/pySlipQt',
#      author='Ross Wilson',
#      author_email='rzzzwilson@gmail.com',
#      license='MIT',
#      packages=find_packages(),
#                  ],
#      install_requires=['pyqt5', 'python'],
#      classifiers=['Development Status :: 3 - Alpha',
#                   'Intended Audience :: Developers',
#                   'License :: OSI Approved :: MIT License',
#                   'Operating System :: OS Independent',
#                   'Programming Language :: Python :: 3 :: Only'],
#      keywords='python pyqt5 slipmap map',
#      download_url='https://github.com/rzzzwilson/pySlipQt/releases/tag/0.1.0',
#      include_package_data=True,
#      zip_safe=False)
