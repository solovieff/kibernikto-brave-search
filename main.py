import asyncio
from typing import List

from kibernikto.bots.cybernoone import Kibernikto
from kibernikto.interactors.tools import get_tools_from_module, Toolbox
from kibernikto.telegram import comprehensive_dispatcher
from kibernikto.utils.environment import configure_logger, print_banner
from kiberbrave import tools


async def start_aiogram(tools_to_use: List[Toolbox]):
    configure_logger()
    print_banner()

    await comprehensive_dispatcher.async_start(Kibernikto, tools_to_use)


# Initialize bot and dispatcher. Main part.
if __name__ == '__main__':
    # get the tools from tool module
    tools_definitions: List[Toolbox] = get_tools_from_module(tools, permitted_names=['search_the_web'])

    for tool in tools_definitions:
        print(f"\n\tApplying {tool.function_name} tool")

    comprehensive_dispatcher.start(bot_class=Kibernikto, tools=tools_definitions, msg_preprocessor=None)
