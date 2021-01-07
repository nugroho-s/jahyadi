import time
from abc import ABC, abstractmethod
from collections import deque


class Command(ABC):
    execution_durations = deque(maxlen=100)


    @abstractmethod
    async def do_response(self, message, args):
        pass

    async def process(self, message, args):
        start_time = time.time()
        await self.do_response(message, args)
        Command.execution_durations.append(round((time.time() - start_time) * 1000, 2))
