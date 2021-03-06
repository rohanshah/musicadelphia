var musicApp = angular.module('musicApp', []);

musicApp.controller('MusicCtrl', function ($scope, $http) {

	$scope.events = {};
	$scope.venues = [ "Union Transfer", "Milkboy", "Electric Factory"
					, "Boot & Saddle"];

	$scope.venueFilter = {};
	for (venue in $scope.venues) {
		$scope.venueFilter[$scope.venues[venue]] = true;
	}

	$http.get('events').success(function (result) {
		$scope.events = result;
	});
});
