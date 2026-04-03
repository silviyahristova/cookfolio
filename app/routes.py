from flask import Blueprint , render_template, request, flash, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/discover')
def discover():
    return render_template('discover.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        # Validation
        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'error')
            return render_template('register.html')
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        else:
            flash('Registration successful!', 'success')
            return render_template('login.html')
    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/support')
def support():
    return render_template('support.html')