function ViewModel() {
  var self = this;

  self.isStairsOn = ko.observable(true);
  self.isOutsideOn = ko.observable(false);   

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
  self.stairsOnClick = function() {

    $.ajax({
      type: "GET",
      url: "/stairs",
      failure: function(errMsg) {
        alert(errMsg);
      },
      success: function(data) {
        self.getFrontdoorGroupState();
      }
    });
  };
  self.outsideOnClick = function() {

    $.ajax({
      type: "GET",
      url: "/outside",
      failure: function(errMsg) {
        alert(errMsg);
      },
      success: function(data) {
        self.getFrontdoorGroupState();
      }
    });
  };
  self.stairsOffClick = function() {

    $.ajax({
      type: "GET",
      url: "/stairs",
      failure: function(errMsg) {
        alert(errMsg);
      },
      success: function(data) {
        self.getFrontdoorGroupState();
      }
    });
  };
  self.outsideOffClick = function() {

    $.ajax({
      type: "GET",
      url: "/outside",
      failure: function(errMsg) {
        alert(errMsg);
      },
      success: function(data) {
        self.getFrontdoorGroupState();
      }
    });
  };

  self.getFrontdoorGroupState = function() {
    
    $.getJSON("/frontdoorgroupstate", function(data) { 
      self.isStairsOn(data[1]);
      self.isOutsideOn(data[0]); 
    });
  };
}

viewModel = new ViewModel();
ko.applyBindings(viewModel);
viewModel.getFrontdoorGroupState();
