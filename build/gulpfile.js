'use strict';

// Require modules
let watchify = require('watchify'),
    browserify = require('browserify'),
    gulp = require('gulp'),
    notify = require('gulp-notify'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    sourcemaps = require('gulp-sourcemaps'),
    assign = require('lodash.assign'),
    gutil = require('gulp-util'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    compass = require('gulp-compass'),
    livereload = require('gulp-livereload'),
    plumber = require('gulp-plumber'),
    ignore = require('gulp-ignore'),
    argv = require('yargs').argv,
    gulpif = require('gulp-if');

// Project variables & Watchify conf
let distFolder = '../core/static/core',
    buildFolder = '../build',
    customOpts = {
        entries: [buildFolder + '/js/app.js'],
        debug: true
    },
    opts = assign({}, watchify.args, customOpts),
    b = watchify(browserify(opts));

// -- TASKS --


// JS Task
gulp.task('javascript', bundle);
b.on('update', bundle);
b.on('log', gutil.log);

function bundle() {

    return b.bundle()
        // log errors if they happen
        .on('error', gutil.log.bind(gutil, 'Browserify Error'))
        .pipe(source('app.js'))
        // optional, remove if you don't need to buffer file contents
        .pipe(buffer())
        // .pipe(gulpif(argv.production, uglify()))
        .pipe(uglify())
        // optional, remove if you dont want sourcemaps
        .pipe(sourcemaps.init({
            loadMaps: true
        })) // loads map from browserify file
        // Add transformation tasks to the pipeline here.
        .pipe(sourcemaps.write('./')) // writes .map file
        .pipe(gulp.dest(distFolder + '/js'));


}

// Lint Task
gulp.task('lint', function() {
    return gulp.src(buildFolder + 'js/*.js')

    .pipe(jshint())
        .pipe(jshint.reporter('default'))
        .on('error', function(err) {
            console.log(err);
        });
});


// Compile our Sass
gulp.task('compass', function() {
    return gulp.src(buildFolder + 'sass/*.sass')
        .pipe(plumber())
        .pipe(compass({
            style: argv.production ? 'compressed' : 'expanded',
            css: distFolder + '/css',
            sass: buildFolder + '/sass',
            image: distFolder + '/img',
            generated_images_path: distFolder + '/img/sprites'
        }))
        .pipe(gulp.dest(distFolder + 'css'));
});



// Watch Files For Changes
gulp.task('watch', function() {
    livereload.listen();


    gulp.watch([distFolder + '/templates/*.html'], function(event) {
        gulp.src(event.path)
            .pipe(plumber())
            .pipe(livereload())
            .pipe(notify({
                title: 'Gulp notice',
                message: event.path.replace(__dirname, '').replace(/\\/g, '/') + ' was ' + event.type + ' and reloaded'
            }));
    });
    gulp.watch(buildFolder + '/js/*.js', ['lint', 'javascript']);
    gulp.watch(buildFolder + '/sass/*.{sass,scss}', ['compass']);
    gulp.watch(buildFolder + '/sass/**/*.{sass,scss}', ['compass']);
});


// Default Task
gulp.task('default', ['lint', 'compass', 'javascript']);
