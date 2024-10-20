from aiogram import Router, types, F
import asyncio
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.for_navigate import tasks_keyboard
from aiogram.utils.formatting import Bold, Underline, as_marked_section, as_section

tasks_router = Router()
TASK = []


@tasks_router.message(F.text == 'tasks')
@tasks_router.message(Command('tasks'))
async def tasks(message: types.Message):
    await message.reply('Выберите действие:', reply_markup=tasks_keyboard)


@tasks_router.message(F.text == 'check all')
async def check_all(message: types.Message):
    if not TASK:
        await message.reply('У вас пока нет задач.', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.reply('Все ваши задачи:', reply_markup=types.ReplyKeyboardRemove())
        for i, task in enumerate(TASK, 1):
            await asyncio.sleep(0.4)
            text = f'✅ {Underline(i)} {Bold(task)}'
            await message.answer(text, parse_mode=types.ParseMode.HTML)


class AddTask(StatesGroup):
    content = State()


@tasks_router.message(StateFilter(None), F.text == 'add a new task')
async def add_new_task(message: types.Message, state: FSMContext):
    await message.answer('Введите задачу:', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddTask.content)


@tasks_router.message(AddTask.content, F.text)
async def add_task_to_list(message: types.Message, state: FSMContext):
    task_content = message.text
    TASK.append(task_content)
    await message.answer(f'Задача "{task_content}" добавлена.', reply_markup=tasks_keyboard)
    await state.clear()
