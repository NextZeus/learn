var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Animal1 = (function () {
    function Animal1(theName) {
        this.name = theName;
    }
    Animal1.prototype.move = function (distanceInMeters) {
        if (distanceInMeters === void 0) { distanceInMeters = 0; }
        console.log(this.name + " moved " + distanceInMeters + "m.");
    };
    return Animal1;
}());
var Snake1 = (function (_super) {
    __extends(Snake1, _super);
    function Snake1(name) {
        _super.call(this, name);
    }
    Snake1.prototype.move = function (distanceInMeters) {
        if (distanceInMeters === void 0) { distanceInMeters = 5; }
        console.log("Slithering...");
        _super.prototype.move.call(this, distanceInMeters);
    };
    return Snake1;
}(Animal1));
var Horse1 = (function (_super) {
    __extends(Horse1, _super);
    function Horse1(name) {
        _super.call(this, name);
    }
    Horse1.prototype.move = function (distanceInMeters) {
        if (distanceInMeters === void 0) { distanceInMeters = 45; }
        console.log("Galloping...");
        _super.prototype.move.call(this, distanceInMeters);
    };
    return Horse1;
}(Animal1));
var sam1 = new Snake1("Sammy the Python");
var tom1 = new Horse1("Tommy the Palomino");
sam1.move();
tom1.move(34);
