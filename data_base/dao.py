from create_bot import logger
from .base import connection
from .models import User
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from sqlalchemy.exc import SQLAlchemyError
import random


@connection
async def set_user(session, tg_id: int, username: str, full_name: str) -> Optional[User]:
    try:
        print(tg_id)
        user = await session.scalar(select(User).filter_by(id=tg_id))

        member_id = random.randint(1000, 10000)
        if not user:
            new_user = User(id=tg_id, username=username, full_name=full_name, member_id=member_id, score=0)
            session.add(new_user)
            await session.commit()
            logger.info(f"Зарегистрировал пользователя с ID {tg_id}!")
            return member_id
        else:
            logger.info(f"Пользователь с ID {tg_id} найден!")
            # return user
            return member_id
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()


# @connection
# async def add_note(session, user_id: int, content_type: str,
#                    content_text: Optional[str] = None, file_id: Optional[str] = None) -> Optional[Note]:
#     try:
#         user = await session.scalar(select(User).filter_by(id=user_id))
#         if not user:
#             logger.error(f"Пользователь с ID {user_id} не найден.")
#             return None

#         new_note = Note(
#             user_id=user_id,
#             content_type=content_type,
#             content_text=content_text,
#             file_id=file_id
#         )

#         session.add(new_note)
#         await session.commit()
#         logger.info(f"Заметка для пользователя с ID {user_id} успешно добавлена!")
#         return new_note
    
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при добавлении заметки: {e}")
#         await session.rollback()


# @connection
# async def update_text_note(session, note_id: int, content_text: str) -> Optional[Note]:
#     try:
#         note = await session.scalar(select(Note).filter_by(id=note_id))
#         if not note:
#             logger.error(f"Заметка с ID {note_id} не найдена.")
#             return None

#         note.content_text = content_text
#         await session.commit()
#         logger.info(f"Заметка с ID {note_id} успешно обновлена!")
#         return note
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при обновлении заметки: {e}")
#         await session.rollback()


# @connection
# async def get_notes_by_user(session, user_id: int, date_add: str = None, text_search: str = None,
#                             content_type: str = None) -> List[Dict[str, Any]]:
#     try:
#         result = await session.execute(select(Note).filter_by(user_id=user_id))
#         notes = result.scalars().all()

#         if not notes:
#             logger.info(f"Заметки для пользователя с ID {user_id} не найдены.")
#             return []

#         note_list = [
#             {
#                 'id': note.id,
#                 'content_type': note.content_type,
#                 'content_text': note.content_text,
#                 'file_id': note.file_id,
#                 'date_created': note.created_at
#             } for note in notes
#         ]

#         if date_add:
#             note_list = [note for note in note_list if note['date_created'].strftime('%Y-%m-%d') == date_add]

#         if text_search:
#             note_list = [note for note in note_list if text_search.lower() in (note['content_text'] or '').lower()]

#         if content_type:
#             note_list = [note for note in note_list if note['content_type'] == content_type]

#         return note_list
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при получении заметок: {e}")
#         return []


# @connection
# async def get_note_by_id(session, note_id: int) -> Optional[Dict[str, Any]]:
#     try:
#         note = await session.get(Note, note_id)
#         if not note:
#             logger.info(f"Заметка с ID {note_id} не найдена.")
#             return None

#         return {
#             'id': note.id,
#             'content_type': note.content_type,
#             'content_text': note.content_text,
#             'file_id': note.file_id
#         }
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при получении заметки: {e}")
#         return None
    
# @connection
# async def delete_note_by_id(session, note_id: int) -> Optional[Note]:
#     try:
#         note = await session.get(Note, note_id)
#         if not note:
#             logger.error(f"Заметка с ID {note_id} не найдена.")
#             return None

#         await session.delete(note)
#         await session.commit()
#         logger.info(f"Заметка с ID {note_id} успешно удалена.")
#         return note
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при удалении заметки: {e}")
#         await session.rollback()
#         return None
    
    
@connection
async def get_user_by_id(session, tg_id):
    try:
        result = await session.execute(select(User).where(User.id==tg_id))
        user = result.scalar_one_or_none()  # Используем scalar_one_or_none вместо scalars().all()
        f = {
            'id': user.id,
            'member_id': user.member_id,
            'full_name': user.full_name,
            'score': user.score,
        }
        
        return f
    except Exception as e:
        print('dao error:', e)
        return "Произошла ошибка"
    
@connection
async def get_all_users(session) -> Optional[Dict[str, Any]]:
    try:
        result = await session.execute(select(User))
        users = result.scalars().all()

        if not users:
            logger.info(f"Users not found")
            return []

        note_list = [
            {
                'id': user.id,
                'member_id': user.member_id,
                'full_name': user.full_name,
                'score': user.score,
            } for user in users
        ]
        
        return note_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении заметок: {e}")
        return []

@connection
async def delete_all_users(session) -> Optional[Dict[str, Any]]:
    try:
        # User.query.delete()
        pass
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при удалении записей: {e}")
        return []


if __name__ == "__main__":
    get_user_by_id(5654)