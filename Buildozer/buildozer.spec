[app]
title = Sherin
package.name = sherin
package.domain = org.sherin
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,mp3,mp4,wav
version = 1.0
requirements = python3,kivy,plyer,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,RECORD_AUDIO
android.minapi = 21
android.ndk = 23b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 
android.api = 33
android.arch = armeabi-v7a
android.enable_androidx = 1
android.entrypoint = org.kivy.android.PythonActivity
android.logcat_filters = *:S python:D
android.whitelist = 
android.icon = %(source.dir)s/Assets/icon.png
android.presplash = %(source.dir)s/Assets/splash.png
android.allow_backup = 1
android.hardwareAccelerated = 1

# Assets location
include_exts = py,kv,png,jpg,mp3,wav,mp4
assets.source_dir = Assets

[buildozer]
log_level = 2
warn_on_root = 1
# Needed if you use a requirements wheel or something external
# custom source for OpenAI or other voice modules can be defined here

[python]
# Leave blank unless you bundle third-party modules locally
# You can use this to include extra folders:
# source.include_patterns = Assets/*, *.py, *.kv
# source.exclude_patterns = tests/*

# (Optional) Add some packaging optimizations
optimize = 2

