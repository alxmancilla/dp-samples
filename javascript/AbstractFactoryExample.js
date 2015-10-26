﻿// A constructor for defining new cars
function Car( options ) {
  // some defaults
  this.doors = options.doors || 4;
  this.state = options.state || "brand new";
  this.color = options.color || "silver";
 
}

// A constructor for defining new trucks
function Truck( options){
  this.state = options.state || "used";
  this.wheelSize = options.wheelSize || "large";
  this.color = options.color || "blue";
}

//function Vehicle(){}

var abstractVehicleFactory = (function () {
 
  // Storage for our vehicle types
  var types = {};
 
  return {
      getVehicle: function ( type, customizations ) {
          var Vehicle = types[type];
 
          return (Vehicle ? new Vehicle(customizations) : null);
      },
 
      registerVehicle: function ( type, Vehicle ) {
          var proto = Vehicle.prototype;
 
          // only register classes that fulfill the vehicle contract
          if ( proto.drive && proto.breakDown ) {
              types[type] = Vehicle;
          }
 
          return abstractVehicleFactory;
      }
  };
})();
 
 
// Usage:
 
abstractVehicleFactory.registerVehicle( "car", Car );
abstractVehicleFactory.registerVehicle( "truck", Truck );
 
// Instantiate a new car based on the abstract vehicle type
var car = abstractVehicleFactory.getVehicle( "car", {
            color: "lime green",
            state: "like new" } );
// Outputs: true
print( car instanceof Car );
 
 
// Instantiate a new truck in a similar manner
var truck = abstractVehicleFactory.getVehicle( "truck", {
            wheelSize: "medium",
            color: "neon yellow" } );

			
			
// Test to confirm our car was created using the vehicleClass/prototype Car
 
// Outputs: Car object of color "yellow", doors: 6 in a "brand new" state
print( truck );

