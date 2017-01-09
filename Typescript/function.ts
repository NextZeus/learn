
//named function
function add(x:number,y:number):number{
    return x + y;
}

//anonymous[匿名] function
let myAdd = function(x,y){
    return x + y;
}
//whole function type : parameter and return type
let add1:(x:number,y:number)=>number = function(x:number,y:number):number{
    return x + y;
}

//自动识别类型
let add2:(x:number,y:number)=>number = function(x,y){
    return x + y;
}

//Optional Parameters
function buildName(firstName:string, lastName?:string){
    if(lastName){
        return firstName + "." + lastName;
    } else {
        return firstName;
    }
}
// Default Parameters
function buildName1(firstName:string, lastName="Smith"){
    if(lastName){
        return firstName + "." + lastName;
    } else {
        return firstName;
    }
}

//Reset[剩余] Parameters 
function buildName2(firstName:string,...resetOfName:string[]){
    return firstName + "." + resetOfName.join(".");
}
let employeeName = buildName2("Joseph", "Samuel", "Lucas", "MacKinzie");




// Overloads[重载]
let suits = ["hearts", "spades", "clubs", "diamonds"];
// 这样改变后,重载的 pickCard 函数在调用的时候会进行正确的类型检查
function pickCard(x: {suit: string; card: number; }[]): number;
function pickCard(x: number): {suit: string; card: number; };
function pickCard(x): any {
    // Check to see if we're working with an object/array
    // if so, they gave us the deck and we'll pick the card
    if (typeof x == "object") {
        let pickedCard = Math.floor(Math.random() * x.length);
        return pickedCard;
    }
    // Otherwise just let them pick the card
    else if (typeof x == "number") {
        let pickedSuit = Math.floor(x / 13);
        return { suit: suits[pickedSuit], card: x % 13 };
    }
}

let myDeck = [{ suit: "diamonds", card: 2 }, { suit: "spades", card: 10 }, { suit: "hearts", card: 4 }];
let pickedCard1 = myDeck[pickCard(myDeck)];
alert("card: " + pickedCard1.card + " of " + pickedCard1.suit);

let pickedCard2 = pickCard(15);
alert("card: " + pickedCard2.card + " of " + pickedCard2.suit);