from . import main

@main.route('/')
def index():
    return 'I have a blog'