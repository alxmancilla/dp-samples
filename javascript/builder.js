function Director() {
	this.construct = function(builder) {
		builder.step1();
		builder.step2();
		return builder.get();
	}
}
 
function CarBuilder() {
	this.car = null;
	this.step1 = function() {
		this.car = new Car();
	};
	this.step2 = function() {
		this.car.addParts();
	};
	this.get = function() {
		return this.car;
	};
}
 
function TruckBuilder() {
	this.truck = null;
	this.step1 = function() {
		this.truck = new Truck();
	};
	this.step2 = function() {
		this.truck.addParts();
	};
	this.get = function() {
		return this.truck;
	};
}
 
function Car() {
	this.doors = 0;
	this.addParts = function() {
		this.doors = 4;
	};
	this.say = function() {
		log.add("I am a " + this.doors + "-door car");
	};
}
 
function Truck() {
	this.doors = 0;
	this.addParts = function() {
		this.doors = 2;
	};
	this.say = function() {
		log.add("I am a " + this.doors + "-door truck");
	};
}
 
// log helper
var log = (function () {
	var log = "";
	return {
		add: function (msg) { log += msg + "\n"; },
		show: function () { print(log); log = ""; }
	}
})();
 
function run() {
	var shop = new Director();
	var carBuilder = new CarBuilder();
	var truckBuilder = new TruckBuilder();
	var car = shop.construct(carBuilder);
	var truck = shop.construct(truckBuilder);
 
	car.say();
	truck.say();
 
	log.show();
}

run();


var Builder = function() {
  var a = "defaultA";
  var b = "defaultB";
   
  return {
      withA : function(anotherA) {
        a = anotherA;
        return this;
      },
      withB : function(anotherB) {
        b = anotherB; 
        return this;
      },
      build : function() {
        return "A is: " + a +", B is: " + b;
      }
  };
};
 
var builder = new Builder();
 
print(builder.build());
 
var first = builder.withA("a different value for A").withB("a different value for B").build();
 
var second = builder.withB("second different value for B").build();
 
var third = builder.withA("now A is different again").build();
 
print(first);
print(second);
print(third);