import os

import nox

ON_TRAVIS = 'TRAVIS' in os.environ

py36 = '3.6'
py37 = '3.7'
py38 = '3.8'

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
	session.install('-U', '.[lint]')
	session.run('flake8', 'src/')
