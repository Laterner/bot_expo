from flask import Flask, request, render_template, redirect, url_for, flash, make_response, session as cookies
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from data_base.models import User
from data_base.base import connection

app = Flask(__name__)

# Настройка базы данных (используем SQLite для примера)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


@app.route('/', methods=['GET', 'POST'])
async def index():
    message = None
    
    admin_id = cookies.get('admin_id')

    if request.method == 'POST':
        member_id = request.form.get('member_id')
        score = request.form.get('score')
        
        if not member_id or not score:
            message = 'Ошибка: необходимо ввести member_id и score'
        else:
            try:
                member_id = int(member_id)
                score_to_add = int(score)
                
                with Session(engine) as session:
                    user = session.query(User).filter_by(member_id=member_id).first()
                    
                    if not user:
                        user = User(
                            member_id=member_id,
                            score=score_to_add
                        )
                        session.add(user)
                    else:
                        if user.score is None:
                            user.score = score_to_add
                        else:
                            user.score += score_to_add
                    
                    session.commit()

                    try:
                        with open('log_send.txt', 'a') as file: 
                            file.write(f"admin {admin_id} send to user {member_id} {score} points" + '\n')
                    except:
                        print('err')

                    message = f'Успешно! Пользователю {member_id} добавлено {score_to_add} очков. Текущий счет: {user.score}'
                    
            except ValueError:
                message = 'Ошибка: member_id и score должны быть числами'
    
    return render_template('index.html', message=message, admin_id=admin_id)

@app.route('/set_id/<int:admin_id>', methods=['GET', 'POST'])
def admin_set_id(admin_id):
    cookies['admin_id'] = admin_id

    return redirect(url_for('index'))

@app.route('/admin')
def admin_page():
    return render_template('send_message.html')

@connection
async def get_users(session):
    result = await session.execute(select(User).order_by(User.id))
    users = result.scalars().all()
    session.close()
    return users

@connection
async def get_user(session, user_id: int):
    result = await session.execute(select(User).where(User.id==user_id))
    user = result.scalar_one_or_none()
    return user

@connection
async def save_user(session, request, user_id: int):
    result = await session.execute(select(User).where(User.id==user_id))
    user = result.scalar_one_or_none()
    
    user.full_name = request.form['full_name']
    # user.score = int(request.form['score'])
    await session.commit()
    return user

@app.route('/users')
async def user_list():
    users = await get_users()
    return render_template('user_list.html', users=users)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
async def edit_user(user_id):
    # session = Session()
    user = await get_user(user_id) # session.query(User).filter_by(id=user_id).first()
    print('request::', request)
    if request.method == 'POST':
        user = await save_user(request, user_id)
        return redirect(url_for('edit_user', user_id=user_id))
    
    # session.close()
    return render_template('edit_user.html', user=user)


if __name__ == '__main__':
    app.secret_key = "AAFPRUZ_Du3bYempDzUXsWHCvRm4RTrg8NQ"
    app.run(host="0.0.0.0")
    