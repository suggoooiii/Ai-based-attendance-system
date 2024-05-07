
from . import bp

@bp.route('/example')
def example():
    return 'Hello, API!'