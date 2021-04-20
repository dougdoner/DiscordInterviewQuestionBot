from tinydb import TinyDB, Query
from discord.ext import commands
import secret

question_db = TinyDB('./database/questions.json')
question_db.insert(
    {'question name': 'test question', 'question text': 'here is some question text', 'difficulty': 'easy'})
question_db.insert(
    {'question name': 'hard test question', 'question text': 'Boy this question sure is hard', 'difficulty': 'hard'})

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def question(ctx, arg):
    """Gets a random question from the database"""
    question_categories = ["easy", "medium", "hard"]
    if arg not in question_categories:
        raise commands.BadArgument('question category must be ' + ", ".join(question_categories))
    question_query = Query()
    questions = question_db.search(question_query.difficulty == arg)
    question_size = len(questions)
    await ctx.send("{0} -- {1}".format(questions[0]["question name"], questions[0]["question text"]))


@question.error
async def question_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(error)


bot.run(secret.config_key)
