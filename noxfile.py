import os
import shutil

import nox

py36 = '3.6'
py37 = '3.7'
py38 = '3.8'

ON_TRAVIS = 'TRAVIS' in os.environ


@nox.session(python=py37)
def lint(session):
	session.install('.[lint]')
	session.run('flake8', 'src/')
