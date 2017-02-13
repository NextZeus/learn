/**
 * Created by lixiaodong on 17/2/13.
 */

{
    let a = 10;
    var b = 1;
}

// console.log('a: ',a); ReferenceError: a is not defined
//let 命令所在的代码块内有效; let 变量声明不会提升
// console.log('b: ', b);

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
