[app]
title = Sherin3
package.name = sherinapp
package.domain = org.sherin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 0.1
requirements = python3,kivy,playsound
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,RECORD_AUDIO

android.api = 31
android.minapi = 21
android.ndk = 23.1.7779620
android.ndk_api = 21
android.target = android-31
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = 1
copy_libs = 1
android.archs = arm64-v8a,armeabi-v7a

# Only add if using modules like playsound or complex audio
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
