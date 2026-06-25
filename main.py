import os
import sys
import threading

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_gastos.settings')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    import django
    django.setup()

    from django.conf import settings
    from django.core.management import call_command
    from django.core.wsgi import get_wsgi_application

    if 'ANDROID_PRIVATE' in os.environ:
        settings.DATABASES['default']['NAME'] = os.path.join(os.environ['ANDROID_PRIVATE'], 'expenses.db')
        settings.DEBUG = False
        settings.ALLOWED_HOSTS = ['*']

    call_command('migrate')

    application = get_wsgi_application()

    from wsgiref.simple_server import make_server

    server = make_server('127.0.0.1', 8520, application)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    from jnius import autoclass

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WebView = autoclass('android.webkit.WebView')

    activity = PythonActivity.mActivity

    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    webview.getSettings().setDomStorageEnabled(True)
    webview.loadUrl('http://127.0.0.1:8520')

    activity.setContentView(webview)

except Exception as e:
    log_path = os.path.join(os.environ.get('ANDROID_PRIVATE', '/data/data/com.expensetracker.app/files'), 'error.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'w') as f:
        f.write(f'{type(e).__name__}: {e}\n')
        import traceback
        traceback.print_exc(file=f)
