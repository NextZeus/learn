// 泛型
// T 类型变量 自动捕捉变量类型 
// 适用于多个类型的函数 叫泛型
function identity<T>(arg:T):T{
    return arg;
}

// 没必要使用 <> 来明确地传入类型 编译器可以查看
let output = identity<string>("log");
let output1 = identity("mylog");