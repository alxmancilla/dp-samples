function add(x, y) { return x + y; }
function sub(x, y) { return x - y; }
 
var Command = function (execute, undo, value) {
    this.execute = execute;
    this.undo = undo;
    this.value = value;
}

var AddCommand = function (value) {
    return new Command(add, sub, value);
};
 
var SubCommand = function (value) {
    return new Command(sub, add, value);
};
 
 
var Calculator = function () {
    var current = 0;
    var commands = [];
 
    function action(command) {
        var name = command.execute.toString().substr(9, 3);
        return name.charAt(0).toUpperCase() + name.slice(1);
    }
 
    return {
        execute: function (command) {
            current = command.execute(current, command.value);
            commands.push(command);
            print(action(command) + ": " + command.value);
        },
 
/*
        undo: function () {
            var command = commands.pop();
            current = command.undo(current, command.value);
            print("Undo " + action(command) + ": " + command.value);
        },
*/ 
        getCurrentValue: function () {
            return current;
        }
    }
}
 
function run() {
    var calculator = new Calculator();
    // issue commands
    calculator.execute(new AddCommand(100));
    calculator.execute(new SubCommand(24));
    
    // reverse last two commands
//    calculator.undo();
//    calculator.undo();
 
    print("\nValue: " + calculator.getCurrentValue());
}

run();