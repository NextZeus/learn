var a = 10;

function f(){
    var msg = '';
    return msg;
}

function f1(){
    var a = 10;
    return function g(){
        var b = a +1;
        return b;
    }
}

var g = f1(); //11

for (var i = 0; i < 10; i++) {
    setTimeout(function() { console.log(i); }, 100 * i);
}//10 10 10 10 10 10 10 10 10 10

for (let i = 0; i < 10; i++) {
    setTimeout(function() { console.log(i); }, 100 * i);
}// 1 2 3 4 5 6 7 8 9 10

for (var i = 0; i < 10; i++) {
    (function(i){
        setTimeout(function() { console.log(i); }, 100 * i);
    })(i);
}//// 1 2 3 4 5 6 7 8 9 10

// let a = 10; var 和 let 不能重复定义同一个变量

const b = 10;
// b = 100; const 常量 不允许修改

//default values
function keepWholeObject(wholeObject:{a:string, b?:number}):void{
    // keepWholeObject now has a variable for wholeObject as well as the properties a and b, even if b is undefined.
}

type C = {a:string, b:number};
function h({a,b}:C):void{

}

function j({a,b} = {a:'',b:0}):void{

}

function k({a, b = 0} = {a: ""}):void{

}
k({a: "yes"}) // ok, default b = 0
k() // ok, default to {a: ""}, which then defaults b = 0
// k({}) // error, 'a' is required if you supply an argument