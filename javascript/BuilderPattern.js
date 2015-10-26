function testBuilderPattern() {
	var shop = new Director();
	var carBuilder = new CarBuilder();
	var car = shop.construct(carBuilder);
	
	car.doSomething();
	
}
function Director() {
	this.construct = function(builder) {
		builder.step1();
		builder.step2();
		return builder.getResult();
	}
}

function CarBuilder(){
	this.car = null;
	this.step1 = function(){
		this.car = new Car();
	}
	this.step2 = function(){
		this.car.addParts();
	}
	this.getResult = function(){
		return this.car;
	}
	
}

function Car(){
	this.doors = 0;
	
	this.addParts  = function(){
		this.doors = 4
	}
	
	this.doSomething = function(){
		print("Tengo " + this.doors +" puertas");
	}
	
}

testBuilderPattern();

 