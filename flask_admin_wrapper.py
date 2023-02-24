def check_admin(name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.username != 'Admin' or current_user.username != 'admin':
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator
  
  
@app.route('/')
@check_admin('function')
def function():
  return render_template()
