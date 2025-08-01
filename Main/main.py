[app]
title = Sherin AI
package.name = sherinai
package.domain = org.sherin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,mp4
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 
android.permissions = INTERNET,RECORD_AUDIO
android.arch = armeabi-v7a

[buildozer]
package.filename = SherinAI.apk
