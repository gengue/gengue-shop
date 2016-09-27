angular.module('cart', ['ui-notification'])

.config(['$interpolateProvider', 'NotificationProvider', function($interpolateProvider, NotificationProvider){
    $interpolateProvider.startSymbol('<%');
    $interpolateProvider.endSymbol('%>');
    NotificationProvider.setOptions({
      delay: 4000,
      startTop: 20,
      startRight: 10,
      verticalSpacing: 20,
      horizontalSpacing: 20,
      positionX: 'right',
      positionY: 'bottom'
    });
}])

.service('CartService', ['$http', function($http){
    this.cart = JSON.parse(localStorage.getItem('cart')) || null;
    this.allProducts = JSON.parse(_PRODUCTS).map(function(item){
      var obj = item.fields;
      obj.id = item.pk;
      return obj; 
    });

    this.handleError = function(res){
      console.warn(res);
    };

    this.getCart = function(){
      return this.cart;
    };

    this.setCart = function(cart){
      this.cart = localStorage.setItem('cart', JSON.stringify(cart));
    };

    this.getAllProducts= function(){
      return this.allProducts;
    };

    this.clear = function(){
      this.cart = null; 
      localStorage.clear();
    };

    this.checkout = function(data, callback){
      return $http.post('/comprar/', data)
              .then(callback, this.handleError) 
    }
}])

.controller('HomeCtrl', ['$scope', 'CartService', 'Notification', '$timeout', function($scope, CartService, Notification, $timeout) {

  $scope.allProducts = CartService.getAllProducts();
  $scope.cart = CartService.getCart();
  $scope.isAuthenticated = _USER;

  if (!$scope.cart) {
    $scope.cart = {};
    $scope.cart.products = [];
  }

  $scope.addProduct = function(id, units){
    var item = _.find($scope.cart.products, function(obj){ return obj.id == id }); 
    if(item) {
      item.units += units ? units : 1; 
    } else {
      item = _.find($scope.allProducts, function(obj){ return obj.id == id }); 
      item.units = units || 1;
      console.log(item);
      $scope.cart.products.push(item); 
    }
    CartService.setCart($scope.cart);    
    Notification.success('Producto agregado al carrito');
  };

  $scope.removeProduct = function(id){
    var item = _.find($scope.cart.products, function(obj){ return obj.id == id }); 
    $scope.cart.products.splice(_.indexOf($scope.cart.products, item), 1)
    CartService.setCart($scope.cart);    
    Notification.error('Producto eliminado del carrito');
  };

  $scope.openAuthModal = function(){
    $('#authModal').modal('show'); 
  }

  $scope.calcTotal = function(){
    var total = 0; 
    angular.forEach($scope.cart.products, function(item){
      total += parseInt(item.units) * parseInt(item.price);
    });
    return total;
  };

  $scope.checkout = function(){
    CartService.checkout($scope.cart, function(data){
      if (data.data.status == 201) {
        CartService.clear();
        Notification.success('Transacion completada!');
        $timeout(function(){
          window.location.href='/';
        }, 2000);
      } else {
        console.error(data); 
        Notification.error('Ocurrio un error!');
      }
    });
  };

}])
.filter('removeHTMLTags', function() {
	return function(text) {
		return  text ? String(text).replace(/<[^>]+>/gm, '') : '';
	};
});






