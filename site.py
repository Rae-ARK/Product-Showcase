from arklight import Site
from pages.home import home
from pages.redmi9a import redmi9a
from pages.pocof4 import pocof4
from pages.neo10r import neo10r
from pages.compare import compare
from pages.gallery import gallery

site = Site()


@site.page("/")
def _home():
    return home()


@site.page("/redmi9a")
def _redmi9a():
    return redmi9a()


@site.page("/pocof4")
def _pocof4():
    return pocof4()


@site.page("/neo10r")
def _neo10r():
    return neo10r()


@site.page("/compare")
def _compare():
    return compare()


@site.page("/gallery")
def _gallery():
    return gallery()
