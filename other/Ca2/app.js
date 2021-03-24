// CODE By: Banuka Vidusanka Paniyan Duwage

const item_list = document.querySelector('#item_list');
const tot_cost = document.querySelector('#tot_cost');
const tot_potion = document.querySelector('#tot_potion');

const btn_clear = document.querySelector('#btn_clear');
//variables to hold each menu item details
const inp_m01 = document.querySelector('#inp_m01');
const btn_m01 = document.querySelector('#btn_m01');
const inp_m02 = document.querySelector('#inp_m02');
const btn_m02 = document.querySelector('#btn_m02');
const inp_m03 = document.querySelector('#inp_m03');
const btn_m03 = document.querySelector('#btn_m03');
const inp_m04 = document.querySelector('#inp_m04');
const btn_m04 = document.querySelector('#btn_m04');
const inp_m05 = document.querySelector('#inp_m05');
const btn_m05 = document.querySelector('#btn_m05');
const inp_m06 = document.querySelector('#inp_m06');
const btn_m06 = document.querySelector('#btn_m06');


const cash_amt = document.querySelector('#cash_amt');
const btn_cancel = document.querySelector('#btn_cancel');
const change_amt = document.querySelector('#change_amt');

//variables to hold total potions and cost
let calcTot = 0;
let calcPotions = 0;

//clear button will clear POTIONS field in each menu item
btn_clear.addEventListener('click', () => {
    console.log('Clear Fields');
    inp_m01.value=''; inp_m02.value=''; inp_m03.value=''; 
    inp_m04.value=''; inp_m05.value=''; inp_m06.value=''; 
});

btn_m01.addEventListener('click', () => {
    console.log('Add item 01');
    calcItemCost('Original Chicken: ',inp_m01.value,3); //call function to calc item cost
});
btn_m02.addEventListener('click', () => {
    console.log('Add item 02');
    calcItemCost('Sweet & Spicy: ',inp_m02.value,5); //call function to calc item cost
});
btn_m03.addEventListener('click', () => {
    console.log('Add item 03');
    calcItemCost('Garlic Chicken: ',inp_m03.value,4); //call function to calc item cost
});
btn_m04.addEventListener('click', () => {
    console.log('Add item 04');
    calcItemCost('Freakin Hot: ',inp_m04.value,2); //call function to calc item cost
});
btn_m05.addEventListener('click', () => {
    console.log('Add item 05');
    calcItemCost('Snowing Vegetable: ',inp_m05.value,4); //call function to calc item cost
});
btn_m06.addEventListener('click', () => {
    console.log('Add item 06');
    calcItemCost('Lemon Chicken: ',inp_m06.value,6); //call function to calc item cost
});

// function to calculate cost of each food item potions
function calcItemCost(name_m,val_m,price) {
    if(val_m<0 || val_m==''){
        console.log('Potions must be a positive number!');
        presentAlert('Potions must be a positive number.');
        return;
    }
    //new ionitem is created everytime a menu item is added
    const newItem = document.createElement('ion-item');
    newItem.textContent = name_m + val_m + ' Potions at Cost: $'+val_m*price;
    item_list.appendChild(newItem);
    calcTot = calcTot + (val_m*price) ;
    tot_cost.textContent = calcTot;
    calcPotions = calcPotions + (val_m*1);
    tot_potion.textContent = calcPotions;
}

//function to present ionic alert
function presentAlert(msg) {
    const alert = document.createElement('ion-alert');
    alert.cssClass = 'my-custom-class';
    alert.header = 'Error!';
    alert.message = msg;
    alert.buttons = ['OK'];
    document.body.appendChild(alert);
    return alert.present();
  }

  //calculate change button event
  document.querySelector('#btn_calc').addEventListener('click', () => {
    console.log('Calculate change');
    var change_calc = cash_amt.value - calcTot;

    if(cash_amt<0){
        presentAlert('Cash amount must be a positive number.');
        return;
    }else if(calcTot<=0){
        presentAlert('Add items from menu first.');
        return;
    }else if(change_calc<0){
        presentAlert('Not enough cash paid.');
        return;
    }

    console.log(change_amt);
    change_amt.textContent = change_calc;
});

//cancel button would reset values and refresh the page
document.querySelector('#btn_cancel').addEventListener('click', () => {
    console.log('Cancel cash payment');
    cash_amt.value='';
    change_amt.textContent = '';
    window.location.reload(); //reload page
});


//simple code to display realtime  DAte & time
  document.querySelector('#todaydate').innerHTML  = new Date().toDateString();

//button to go to main app on github-home btn - CA1
document.querySelector('#btn_home').addEventListener('click', () => {
    console.log('redirecting to github page');
    window.location.href = 'https://banukaknight.github.io/LPU-CAP917-MApp/';
});
  