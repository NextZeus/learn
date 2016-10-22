//理解：接口参数类型定义

interface LabelledValue {
    label: string;
}

function printLabel(labelledObj: LabelledValue) {
    console.log(labelledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);

interface SquareConfig {
    color?: string;
    width?: number;
}

//后面的interface会覆盖之前的定义  之前的color可省略 
function createSquare(config: SquareConfig): {color: string; area: number} {
    let newSquare = {color: "white", area: 100};
    if (config.color) {
        newSquare.color = config.color;
    }
    if (config.width) {
        newSquare.area = config.width * config.width;
    }
    return newSquare;
}

let mySquare = createSquare({color: "black"});

/*
// error: 'colour' not expected in type 'SquareConfig'
let mySquare0 = createSquare({ colour: "red", width: 100 });
interface SquareConfig {
    color?: string;
    width?: number;
    [propName: string]: any;  定义不可预测的变量 colour 
}
*/


let mySquare1 = createSquare({ width: 100, opacity: 0.5 } as SquareConfig);


// Readonly properties
/* 检测到语法错误
interface Poinf{
    readonly x:number;
    readonly y:number;
}

let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
ro[0] = 12; // error!
ro.push(5); // error!
ro.length = 100; // error!
a = ro; // error!

*/


// Fucntion Types

interface SearchFunc {
    (source: string, subString: string): boolean;
}

let mySearch: SearchFunc;
mySearch = function(source: string, subString: string) {
    let result = source.search(subString);
    if (result == -1) {
        return false;
    }
    else {
        return true;
    }
}

//the names of the parameters do not need to match 参数名 不需要匹配
mySearch = function(src: string, sub: string): boolean {
    let result = src.search(sub);
    if (result == -1) {
        return false;
    }
    else {
        return true;
    }
}


// Indexable Types
interface StringArray {
    [index:number]  :string;
}

let myArray : StringArray;
myArray = ['Bob','Fred'];

class Animal {
    name:string;
}

class Dog extends Animal{
    breed:string;
}

// Class Types
interface ClockInterface{
    currentTime:Date;
}

class Clock implements ClockInterface{
    currentTime:Date;
    constructor(h:number, m:number){

    }
}

// Extending Interfaces
interface Shape {
    color: string;
}

interface PenStroke {
    penWidth: number;
}

interface Square extends Shape, PenStroke {
    sideLength: number;
}

let square = <Square>{};
square.color = "blue";
square.sideLength = 10;
square.penWidth = 5.0;


