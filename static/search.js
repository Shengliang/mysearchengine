angular
  .module('MyApp')
  .controller('SearchController', function($scope, $http) {
    $scope.user = {
      searchTerm: ''
    };
    
    $scope.someFunction = function() {
        $scope.message = {};
        var responsePromise = $http(
        {
            url: "search", 
            method: "POST",
            params: {search: $scope.user.searchTerm}
         }).success(function(data, status, headers, config) {
              $scope.message = data;
          }).error(function(data, status, headers, config) {
              $scope.message = data;
        });
    };
  });