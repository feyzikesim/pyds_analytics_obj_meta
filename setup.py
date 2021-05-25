from distutils.core import setup
setup (name = 'pyds_analytics',
       version = '1.0',
       description = """Install precompiled DeepStream Python bindings for tracker metadata extension""",
       packages=[''],
       package_data={'': ['pyds_analytics.so']},
       )
