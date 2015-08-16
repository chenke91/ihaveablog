'use strict';

var myApp = angular.module('myApp', ['ui.bootstrap']);

myApp.controller('BlogListController', function($scope, $http){
    $scope.blogs = {
        categories: [],
        blogs: [],
        get_cates: function() {
            $http.get('/admin/api/categories/').success(function(resp) {
                $scope.blogs.categories = resp.data;
            });
        },
        get_blogs: function() {
            $http.get('/admin/api/blogs/').success(function(resp) {
                $scope.blogs.blogs = resp.data;
            })
        },
        init: function() {
            this.get_cates();
            this.get_blogs();
        }
    };
    $scope.blogs.init();
}).filter('get_cate_byid', function() {
    var get_cate_byid = function(id, categories) {
        var cate = _.find(categories, function(item) {return item.id==id});
        if (cate)
            return cate.name;
        return '';
    };
    return get_cate_byid;
});