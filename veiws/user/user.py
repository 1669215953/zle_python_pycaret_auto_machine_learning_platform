from flask import Flask,session,render_template,redirect,Blueprint,request
from utils.DBmanager import DBmanager
from utils.errorresponse import errorresponse
ub = Blueprint('user',__name__,url_prefix='/user',template_folder='templates')
@ub.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        def filter_fn(user) :
            return request.form['username'] in user and request.form['password'] in user
        users=DBmanager.query('select * from user',[],'select')
        print(users)
        login_success = list(filter(filter_fn ,users))
        if not len(login_success): return errorresponse('账号或密码错误')
        session['username' ] = request.form[ 'username']
        return redirect("/up_data")



@ub.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if request.form[ 'password'] != request.form[ 'checkpassword']:
            return errorresponse('两次密码不符合')

        def filter_fn(user):
            return request.form['username'] in user

        users = DBmanager.query('select * from user', [],'select')#找到全部用户
        print(users)
        filter_list=list(filter(filter_fn,users))#过滤掉其他不同名
        print(filter_list)

        if len(filter_list):
         return errorresponse('该用户已被注册')
        else:
            DBmanager.register_user(request.form[ 'username'],request.form[ 'password'])
            return redirect('/user/login')
@ub.route('/logOut')
def logout():
    session.clear()
    return redirect('/user/login')