var gulp = require("gulp");
var ts = require("gulp-typescript");
var sass = require("gulp-sass");
var minifyCss = require("gulp-minify-css");
var rename = require("gulp-rename");
var uglify = require('gulp-uglify');

gulp.task("build-ts", function () {

    var tsOptions = {
        target: "ES5",
        out: "main.js"
    };

    var tsCompile = gulp.src("scripts/typescript/**/*.ts").pipe(ts(tsOptions));

    return tsCompile.js
        .pipe(uglify())
        .pipe(rename("main.min.js"))
        .pipe(gulp.dest("scripts"));
});

gulp.task("build-sass", function () {

    return gulp.src("css/scss/*.scss").pipe(sass())
        .pipe(minifyCss())
        .pipe(rename("main.min.css"))
        .pipe(gulp.dest("css"));
});

gulp.task("build", ["build-ts", "build-sass"]);

gulp.task("default", ["build"]);
