let deck = {
    suits: ["hearts", "spades", "clubs", "diamonds"],
    cards: Array(52),
    createCardPicker: function() {
        // error
        /*
        return function() {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {suit: this.suits[pickedSuit], card: pickedCard % 13};
        };
        */
        // 1 bind deck 
        /*
        return function() {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {suit: this.suits[pickedSuit], card: pickedCard % 13};
        }.bind(this);
        */
        // 2 es6箭头函数
        return ()=> {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {suit: this.suits[pickedSuit], card: pickedCard % 13};
        };
    }
}

// this的值在函数被调用的时候才会指定
let cardPicker = deck.createCardPicker();
let pickedCard = cardPicker();//this.suits not exists this->global not deck

console.log("card: " + pickedCard.card + " of " + pickedCard.suit);