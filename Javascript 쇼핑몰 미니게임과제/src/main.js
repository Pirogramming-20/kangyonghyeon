//Fetch the items from the JSON file
function loadItems(){
  return fetch('data/data.json')
  .then(response=>response.json())
  .then(json=>json.items);

}

//loadItems에 json.items가 리턴이 되고 밑에 함수애서 item이라는 변수에 loaditems값이 들어간다

//update the list with given items
function displayItems(items){
  const container = document.querySelector('.items');
  container.innerHTML =items.map(item => createHTMLString(item)).join('');
  //문자열로 바꿔서 join으로 li들 엮어서 출력-> html에 li태그들이 추가된다
}

//create HTML list item from thr given data item
function createHTMLString(item){
  return `
  <li class="item">
    <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
    <span class="item__description">${item.gender} ,${item.size}</span>
  </li>
  `;
}

function setEventListeners(items){
  const logo =document.querySelector('.logo');
  const buttons =document.querySelector('.buttons');
  logo.addEventListener('click',()=>displayItems(items));
  buttons.addEventListener('click',event=> onButtonClick(event,items));

}

function onButtonClick(event,item){
  const dataset=event.target.dataset;
  const key =dataset.key;
  const value =dataset.value;
  if (key==null || value==null){
    return;
  }
  const filtered =item.filter(item=>item[key]===value);
  console.log(filtered)
  displayItems(filtered);

}
//main

loadItems()
.then(items=>{
  console.log(items);
  displayItems(items);
  setEventListeners(items) 
})
.catch(console.log)