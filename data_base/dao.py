from create_bot import logger
from .base import connection
from .models import User
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from sqlalchemy.exc import SQLAlchemyError
import random


async def generate_code(session):
    member_id = random.randint(1000, 10000)
    while u := await session.scalar(select(User).filter_by(member_id=member_id)) != None:
        print(member_id)
        member_id = random.randint(1000, 10000) 
    return member_id

@connection
async def set_user(session, tg_id: int, username: str, full_name: str) -> Optional[User]:
    try:
        print(tg_id)
        user = await session.scalar(select(User).filter_by(id=tg_id))

        member_id = await generate_code(session)
            
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
        result = await session.execute(select(User).order_by(User.score.desc()).limit(15))
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