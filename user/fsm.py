from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Application(StatesGroup):
    cv = State()


class Feedback(StatesGroup):
    feedback = State()
