// Boolean
let isDone : Boolean = false;

// Number
let decimal:number = 6;
let hex:number = 0xf00d;
let binary:number = 0b1010;
let octal:number = 0o744;

// String
let color:string = 'blue';
color = 'red';

//template strings
let fullName:string = 'Bob Bobbington';
let age:number = 28;
let sentence:string = `Hello , my name is ${ fullName }. I'll be ${age + 1} years old next year.`;

// Array
//type[]
let list:number[] = [1,2,3];

//Array<type>
let list1:Array<number> = [1,2,3];

// Tuple
let x:[string, number];
//initial 
x = ["Hello", 10]; //类型必须匹配

// Enum
enum Color {Red=1, Green = 2, Blue = 4}; //2,4 array index
let c:Color = Color.Green;
let colorName:string = Color[2]; //Green

// Any

let notSure:any = 4;
notSure.ifItExists()
notSure.toFixed();

let list2:any[] = [1,'tree',true];

// Void

function warnUser():void{
    console.log('this is my warning');
}







