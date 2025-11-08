from sopel import plugin
# You may also need to import `bot` and `trigger` types for advanced use
# from sopel.bot import SopelWrapper
# from sopel.trigger import Trigger

# import local chopra module
import chopra

@plugin.command('chopra')
def greet(bot, trigger):
    """
    A simple command that responds to '.hello'
    """
    # The 'bot' object is a wrapper around the Sopel instance.
    # The 'trigger' object holds information about the message that triggered the rule.
    # build quote
    chopra_quote = chopra.build_quote()

    # Send a message back to the channel/user
    bot.say(chopra_quote)

    # You can access the sender's nickname via trigger.nick
    # bot.reply(f'Hello there, {trigger.nick}!')

    # You can also get any arguments following the command
    # if trigger.group(2):
    #     bot.say(f'You said: {trigger.group(2)}')


# Example of an optional setup hook
def setup(bot):
    """
    Optional function called when the plugin is loaded.
    Useful for defining configuration sections, database connections, etc.
    """
    # Example: bot.settings.define_section('myplugin', MyPluginSection)
    pass

# Example of an optional shutdown hook
def shutdown(bot):
    """
    Optional function called when the plugin is unloaded or the bot is shut down.
    Useful for cleaning up resources.
    """
    pass
