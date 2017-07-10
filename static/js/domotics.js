function ViewModel() {
  var self = this;
   

  self.screenUpClick = function() {

    $.ajax({
      type: "GET",
      url: "/screen?action=up",
      failure: function(errMsg) {
        alert(errMsg);
      }
    });
  };
  self.screenDownClick = function() {

    $.ajax({
      type: "GET",
      url: "/screen?action=down",
      failure: function(errMsg) {
        alert(errMsg);
      }
    });
  };
  self.garageClick = function() {

    $.ajax({
      type: "GET",
      url: "/garage",
      failure: function(errMsg) {
        alert(errMsg);
      }
    });
  };
  self.allOffClick = function() {

    $.ajax({
      type: "GET",
      url: "/alloff",
      failure: function(errMsg) {
        alert(errMsg);
      }
    });
  };
}

viewModel = new ViewModel();
ko.applyBindings(viewModel);