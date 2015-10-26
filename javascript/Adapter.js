// old interface  Target
 
function Shipping() {
    this.request = function(zipStart, zipEnd, weight) {
        // ...
        return "$49.75";
    }
}
 
// new interface  Adaptee
 
function AdvancedShipping() {
    this.login = function(credentials) { /* ... */ };
    this.setStart = function(start) { /* ... */ };
    this.setDestination = function(destination) { /* ... */ };
    this.calculate = function(weight) { return "$39.50"; };
}
 
// adapter interface
 
function ShippingAdapter(credentials) {
    var shipping = new AdvancedShipping();
 
    shipping.login(credentials);
 
    return {
        request: function(zipStart, zipEnd, weight) {
            shipping.setStart(zipStart);
            shipping.setDestination(zipEnd);
            return shipping.calculate(weight);
        }
    };
}
 
 
function run() {
    var shipping = new Shipping();
    // original shipping object and interface
 
    var cost = shipping.request("78701", "10010", "2 lbs");
    print("Old cost: " + cost);
 
    var credentials = {token: "30a8-6ee1"};
    var adapter = new ShippingAdapter(credentials);
     // new shipping object with adapted interface 
    cost = adapter.request("78701", "10010", "2 lbs");
 
    print("New cost: " + cost);
}

run();