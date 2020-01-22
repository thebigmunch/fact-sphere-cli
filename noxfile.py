import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
	session.install('-U', '.[lint]')
	session.run('flake8', 'src/')
