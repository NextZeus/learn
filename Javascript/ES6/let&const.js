/**
 * Created by lixiaodong on 17/2/13.
 */
'use strict';

{
    let a = 10;
    var b = 1;
}

// console.log('a: ',a); ReferenceError: a is not defined
//let 命令所在的代码块内有效; let 变量声明不会提升
// console.log('b: ', b);

/*
// 0~9
for(var i = 0 ; i < 10 ; i++){
    //or let j = i; console.log('>>', j)
    setTimeout(function (j) {
        console.log('>>',j);
    }.bind(this,i),100);
}

// 0~9
for(let i = 0 ; i < 10 ;i++){
    setTimeout(function () {
        console.log('<<',i);
    },100)
}
*/

/*
//块级作用域
var tmp = new Date();

function f() {
    console.log('tmp: ',tmp);
    if (false) {
        //变量提升 undefined
        var tmp = "hello world";
    }
}

f(); // undefined 变量提升 内层的tmp变量覆盖了外层的tmp变量


var s = 'hello';

for (var i = 0; i < s.length; i++) {
    console.log(s[i]);
}

console.log(i); // 5

*/

//let为js新增了块级作用域
function f1() {
    let n = 5;
    if (true) {
        let n = 10;
    }
    console.log(n); // 5
}

//es6允许块级作用域的任意嵌套
//外层作用域无法读取内层作用域的变量
{{{{
    {let a = 1}
    // console.log(a) ReferenceError: a is not defined
}}}}

//块级作用域的出现 使得立即执行函数表达式IIFE不再必要
/*
(function () {
    var tmp = '';
})();

{
    let tmp = ''
}
    */

//const 常量不可改变 声明变量必须立即初始化
const PI = 3.1415;
const a = [];//数组本身是可写的， 但是如果将另一个数组赋值给a 就会报错
a.push('hello')

// a = ['Dave'] TypeError: Assignment to constant variable.

//模式匹配 解构
let [a,b,c] = [1,2,3];
let [x,y] = [1]//y=undefined
let [head, ...tail] = [1,2,3,4]//head=1, tail=[2,3,4]
//...tail 如果解构不成功 就是[]

