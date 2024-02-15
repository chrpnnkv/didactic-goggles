from flask import Flask
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '.\\static\\img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def start_page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    data = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    return '<br>'.join(data)


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h3>Вот она, красная планета!</h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                     <ul class="list-group">
                          <li class="list-group-item list-group-item-warning">Человечество вырастает из детства.</li>
                          <li class="list-group-item list-group-item-info">Человечеству мала одна планета.</li>
                          <li class="list-group-item list-group-item-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</li>
                          <li class="list-group-item list-group-item-success">И начнем с Марса!</li>
                          <li class="list-group-item list-group-item-danger">Присоединяйся!</li>
                        </ul>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 align="center">Анкета претендента</h2>
                            <h4 align="center">на участие в миссии</h4>
                            <div align="center">
                            <div class="p-3 mb-2" align="left">
                                <form class="login_form" method="post" >
                                    <br>
                                    <input type="text " class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text " class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <br/>
                                     <label for="form-group form-check">Какие у Вас есть профессии?</label>
                                     <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="engineer" name="engineer">
                                                <label class="form-check-label" for="engineer">Инженер-исследователь</label>
                                            <br/>    
                                            <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            <br/>    
                                            <input type="checkbox" class="form-check-input" id="builder" name="builder">
                                                <label class="form-check-label" for="builder">Строитель</label>
                                            <br/>    
                                            <input type="checkbox" class="form-check-input" id="biolog" name="biolog">
                                                <label class="form-check-label" for="biolog">Экзобиолог</label>
                                            <br/>    
                                            <input type="checkbox" class="form-check-input" id="doctor" name="doctor">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            <br/>    
                                            <input type="checkbox" class="form-check-input" id="climat" name="climat">
                                                <label class="form-check-label" for="climat">Климатолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли Вы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        if request.form.get('accept', False):
            data = request.form
            return "Форма отправлена"
        else:
            return "Ошибка заполнения. Вы не готовы!"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    data = f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                         '''
    if planet_name != 'Марс':
        data += f'''<h2 class="text-success">А может лучше всё-таки на Марс?</h2>
                    <h4 class="text-primary">Ведь у него так много преимуществ! Например:</h4>'''
    data += f'''<ul class="list-group">
                              <li class="list-group-item list-group-item-warning">Эта планета близка к Земле;</li>
                              <li class="list-group-item list-group-item-info">На ней много необходимых ресурсов;</li>
                              <li class="list-group-item list-group-item-secondary">На ней есть вода и атмосфера;</li>
                              <li class="list-group-item list-group-item-success">На ней есть небольшое магнитное поле;</li>
                              <li class="list-group-item list-group-item-danger">Наконец, она просто красива!</li>
                        </ul>
                    </body>
                </html>'''
    return data


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h2>
                        <h3 class="p-3 mb-2 bg-success text-white">Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                        <h3 class="p-3 mb-2">составляет {rating}!</h3>
                        <h3 class="p-3 mb-2 bg-warning text-dark">Желаем удачи!</h3>
                      </body>
                    </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 align="center">Загрузка фотографии</h2>
                            <h4 align="center">для участия в миссии</h4>
                            <div class="p-3 mb-2" align="left">
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br/>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save(f'static/img/{f.filename}')
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                                    <title>Пример формы</title>
                                  </head>
                                  <body>
                                    <h2 align="center">Загрузка фотографии</h2>
                                    <h4 align="center">для участия в миссии</h4>
                                    <div class="p-3 mb-2" align="left">
                                        <form class="login_form" method="post" enctype="multipart/form-data">
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <img src="/static/img/{f.filename}" alt="здесь должна была быть картинка" 
                                             width=250px vspace=30px>
                                            <br/>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" 
                            rel="stylesheet" 
                            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" 
                            crossorigin="anonymous">
                            <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" 
                            integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" 
                            crossorigin="anonymous"></script>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Пейзажи Марса</h1>
                            <div id="myCarousel" class="carousel slide" data-ride="carousel">
                                <div class="carousel-indicators">
                                    <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                    <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                    <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                </div>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                        <img src="/static/img/first.jpg" alt="1" class="d-block w-100"> 
                                </div>
                                <div class="carousel-item">
                                        <img src="/static/img/second.jpg" alt="2" class="d-block w-100" > 
                                </div>
                                <div class="carousel-item">
                                        <img src="/static/img/third.jpg" alt="3" class="d-block w-100" > 
                                </div>
                             </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                              </button>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
