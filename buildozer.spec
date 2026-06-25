[app]

title = Expense Tracker
package.name = expensetracker
package.domain = org.iroennys

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,txt,json,otf,ttf,md

version = 1.0.0

requirements = python3, django, sqlite3, setuptools, pyjnius

presplash.color = #1a1a2e

orientation = portrait

android.minapi = 21
android.api = 34
android.ndk = 25b

android.archs = armeabi-v7a

android.permissions = INTERNET

android.add_activity = True
android.wakelock = True

android.accept_sdk_license = True

android.gradle_dependencies = androidx.webkit:webkit:1.12.1

android.allow_backup = True

android.use_shlib = True

[buildozer]

log_level = 2

warn_on_root = 0
