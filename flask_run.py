from flask import Flask, request, render_template
from sqlalchemy import create_engine, Integer, String, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from data_base.models import User


app = Flask(__name__)

# Настройка базы данных (используем SQLite для примера)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    
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
                    message = f'Успешно! Пользователю {member_id} добавлено {score_to_add} очков. Текущий счет: {user.score}'
                    
            except ValueError:
                message = 'Ошибка: member_id и score должны быть числами'
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)