import os
from deploynpm import npm_install
from deploybower import bower_install
from deploygulp import gulp
from deploysync import sync_with_manifest


# Retrieving environment paths

script_dir = os.path.dirname(os.path.abspath(__file__))

repository_dir = os.getenv("DEPLOYMENT_SOURCE")
webserver_dir = os.getenv("DEPLOYMENT_TARGET")

build_in_place_only = False

if not webserver_dir:
    print "No destination deployment location was specified: building only!"
    build_in_place_only = True

if not repository_dir:
    repository_dir = os.path.normpath(os.path.join(script_dir, ".."))

website_build_dir = os.path.join(repository_dir, "website")


# Installing packages

npm_install(website_build_dir)
bower_install(website_build_dir)


# Building the website

gulp(website_build_dir, "build")


# Syncing files to webserver directory

deployment_ignores = [
    ".gitignore",

    # Ignoring package manager configurations
    "node_modules",
    "bower.json",

    # Ignoring NPM modules (used only for build)
    "package.json",

    # Ignoring build script
    "gulpfile.js",

    # Ignoring TypeScript type definitions and sources
    "tsd.json",
    "*.ts",

    # Ignoring SASS files
    "*.scss"
]

if not build_in_place_only:
    sync_with_manifest(website_build_dir, webserver_dir, deployment_ignores)


# Done

print "Finished successfully."
