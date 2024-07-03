[app]
# (str) Title of your application
title = FlashcardApp

# (str) Package name
package.name = flashcardapp

# (str) Package domain (needed for Android)
package.domain = org.yourdomain

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = kivy, python3, hostpython3, sdl2, pyjnius, android

# (str) Application versioning (method 1)
version = 0.1

# (str) Presplash of the application (backwards-compatible with 1.2.0)
# presplash.filename = %(source.dir)s/images/presplash.png

# (list) Permissions
# e.g. android.permissions = INTERNET
#android.permissions = INTERNET

# (str) The type of orientation that the application is
# Valid options are: landscape, sensorLandscape, portrait or sensorPortrait
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25c

[buildozer]
# (int) Log level (0, 1, 2, 3)
log_level = 2

# (bool) Avoid compiling through root
warn_on_root = 1


