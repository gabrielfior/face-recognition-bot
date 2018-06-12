import pytest

from corebot.telegramBot.bot import Bot

@pytest.fixture(scope="module")
def bot() -> Bot:
    return Bot()