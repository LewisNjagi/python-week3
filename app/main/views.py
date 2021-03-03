from flask import render_template,redirect,url_for,abort,request
from . import main
from .forms import CommentForm,PitchForm
from flask_login import login_required,current_user
from ..models import Pitch,User,Comment
from .. import db,photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    return render_template('index.html',pitches = pitches)

@main.route('/category/<category>')
def interview(category):
    '''
    '''
    pitches = Pitch.query.filter_by(category = 'Interview').all()
    return render_template('interview.html',pitches = pitches)

@main.route('/category/sales')
def sales():
    '''
    '''
    pitches = Pitch.query.filter_by(category = 'Sales').all()
    return render_template('sales.html',pitches = pitches)

@main.route('/category/promotion')
def promotion():
    '''
    '''
    pitches = Pitch.query.filter_by(category = 'Promotion').all()

    return render_template('promotion.html',pitches = pitches)

@main.route('/category/pickuplines')
def pickup():
    '''
    '''
    pitches = Pitch.query.filter_by(category = 'Pick Up Lines').all()
    return render_template('pickup.html',pitches = pitches)

# @main.route('/comments/<int:pitches_id>', methods = ['POST','GET'])
# def comments(pitches_id):
#     form = CommentForm()
    

@main.route('/pitch/comment/new/<int:pitches_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitches_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitches_id)
    all_comments = Comment.query.filter_by(pitches_id = pitches_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitches_id = pitches_id
        
        new_comment = Comment(comment = comment,pitches_id = pitches_id,user_id = current_user.id)
        
        new_comment.save_comment()
        return redirect(url_for('.new_comment', pitches_id = pitches_id))


    return render_template('new_comment.html',comment_form = form, pitch = pitch, all_comments = all_comments)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        title = form.title.data

        new_pitch = Pitch(pitch = pitch,title = title,category = category,user_id = current_user.id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html',pitch_form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = current_user.id)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))