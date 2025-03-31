import discord
from discord.ext import commands

class BPCommandError(commands.CommandError):
    def __init__(self, message):
        super().__init__(f"{message}")

class BPError(discord.ApplicationCommandError):
    def __init__(self, message):
        super().__init__(f"{message}")

class ObjectNotFound(BPError):
    def __init__(self):
        super().__init__(f"Object not found")


class ActivityNotFound(BPError):
    def __init__(self, activity: str):
        super().__init__(f"Activity `{activity}` not found")
