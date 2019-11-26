from flask import Flask, render_template, request
import random,requests
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html',html_name=name)
    #return f'안녕, {name}'

#세제곱을 돌려주는 cub 페이지 작성
#사용자한테 숫자값을 받아서 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    #return str(number ** 3)
    result = number ** 3
    return render_template('cube.html',result=result,number=number)

@app.route('/movies')
def movies():
    movie_list = ['82년생김지영','조커','궁예']
    return render_template('movies.html',movies=movie_list)

#ping : 사용자로부터 입력을 받을 Form페이지를 넘겨준다
@app.route('/ping')
def ping():
    return render_template('ping.html')

#pong : 사용자로부터 form데이터를 전달받아서 가공한다
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html',user_name=user_name)

#fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

#전달받은 이름을 기준으로 넘겨줄 각종 정보를 가공해서 돌려주는 (응답)로직
@app.route('/godmademe')
def godmademe():
    #1. 사용자가 입력한 데이터를 가져온다
    user_name = request.args.get('user_name')
    #2. 사용자에게 보여줄 여러가지 재밌는 특정들 리스트를 만든다
    first_list = ['미모들 듬뿍~','착함 세방울 넣고','앗 잘못넣음','엉뚬함 조금 넣고','성실함 두방울 넣고','잘생김 두방울 넣고..엌 쏟았네']
    second_list = ['기럭지도 필요하려나','애교도 조금 넣으면 좋겠군']
    third_list = ['하긴 너무 다 퍼줄 수 없지','기억력을 마지막으로.. 엌 바닥에 쏟았네','성실함을 마지막으로.. 엌 바닥에 쏟았네']
    
    #3. 리스트에서 랜덤으로 하나씩을 선택한다
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    #4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다
    return render_template('godmademe.html',user_name=user_name,first=first,second=second,third=third)

#1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
# 이때 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다.
@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/result')
def result():
    #1.사용자가 입력한 FROM 데이터를 가져온다
    word = request.args.get('word')
    #2. ARTII API로 요청을 보내서 응답 결과를 변수에 담는다 (폰트 정보들)
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    #3. 가져온 폰트들을 리스트 형태로 바꾼다
    fonts = fonts.split('\n')
    #print(fonts)
    #4. 폰트 하나를 랜덤으로 선택한다
    font = random.choice(fonts)
    #5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    #6. 최종 결과물을 사용자에게 돌려준다
    return render_template('artii_result.html',result=result)

#debug 모드를 활성화해서 서버 새로고침을 생략
if __name__ == '__main__':
    app.run(debug=True)