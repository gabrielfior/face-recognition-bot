from corebot.telegramBot.bot import Bot


def test_bot(bot : Bot):
    print(bot)

def test_addOne(bot : Bot):
    assert bot.addOne(1) == 2
    assert Bot.addOne(2) == 3
