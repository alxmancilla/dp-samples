var animal = { eats: true }
var rabbit = { jumps: true }

rabbit.__proto__ = animal  // inherit
print(rabbit.eats) // true

var fedUpRabbit = { eats: false}

fedUpRabbit.__proto__ = animal  
print(fedUpRabbit.eats) // false


print("***__proto__***")
/**  Nueva version **/
var animal = {
  eat: function() { 
    print( "I'm full" )
    this.full = true
  }
}

var rabbit = { 
  jump: function() { /* something */ }
}
rabbit.__proto__ = animal  
rabbit.eat()

print("****Object.create**")
/**  Nueva version **/
rabbit = Object.create(animal)
print( Object.getPrototypeOf(rabbit) === animal ) // true

print("****Rabbit.prototype**")
function Rabbit(name) {
  this.name = name
}
Rabbit.prototype = { eats: true }
var rabbit = new Rabbit('John')
for(var p in rabbit) {
  if (!rabbit.hasOwnProperty(p)) continue // filter out "eats"
  print(p + " = " + rabbit[p]) // outputs only "name"
}