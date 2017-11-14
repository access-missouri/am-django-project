var gulp = require('gulp'),
	gutil = require('gulp-util'),
	compass = require('gulp-compass'),
	shell = require('gulp-shell'),
	webserver = require('gulp-webserver'),
	flatten = require('gulp-flatten'),
	babel = require('gulp-babel')
    uglify = require('gulp-uglify'),
	path = require('path');

gulp.task('test', function(){
	gutil.log('This is a test.');
});

gulp.task('sass', function(){
	gulp.src('./static-components/sass/*.scss')
		.pipe(compass({
			project: path.join(__dirname, 'static-components'),
			css: 'css',
			sass: 'sass',
			require: ['susy']
		}))
		.pipe(flatten())
		.pipe(gulp.dest('static/css'));
});

gulp.task('js', function(){
	return gulp.src('components/js/**/*.js')
		.pipe(babel({
			presets: ['es2015', 'react']
		}))
		// .pipe(uglify())
	.pipe(gulp.dest('static/js'));
});



gulp.task('build', ['js', 'sass']);

gulp.task('deploy', ['build', 'upload']);

gulp.task('watch',function(){
	gutil.log('Gulp will say that this task has finished, but don\'t believe its dirty lies.');
	gutil.log('Hit \^c to actually exit watch mode.');
	gulp.watch('static-components/**/*.js',['js']);
    gulp.watch('static-components/**/*.scss',['sass']);
});