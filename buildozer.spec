[app]

title = Expense Tracker
package.name = expensetracker
package.domain = org.iroennys

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,txt,json,otf,ttf,md

version = 1.0.0

requirements = python3, django, sqlite3, setuptools

presplash.color = #1a1a2e

orientation = portrait

osx.package_name = Expense Tracker

android.minapi = 21
android.api = 34
android.ndk = 25b

android.archs = armeabi-v7a

android.permissions = INTERNET

android.add_activity = True
android.wakelock = True

android.accept_sdk_license = True

android.gradle_dependencies = 'androidx.webkit:webkit:1.12.1'

android.add_src =

android.add_aars =

android.add_jars =

android.private_storage_path =

android.allow_backup = True

android.keystore =

android.keystore.password =

android.keyalias =

android.keyalias.password =

android.manifest.extra = <uses-feature android:glEsVersion="0x00020000" android:required="True" />

android.strings =

android.appclass =

android.use_shlib = True

android.copy_libs =

[buildozer]

log_level = 2

warn_on_root = 0
