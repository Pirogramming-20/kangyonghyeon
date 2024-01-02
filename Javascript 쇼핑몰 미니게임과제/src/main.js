//Fetch the items from the JSON file
function loadItems(){
  return fetch('data/data.json')
  .then(response=>response.json())
  .then(json=>json.items);

}

//loadItems에 json.items가 리턴이 되고 밑에 함수애서 item이라는 변수에 loaditems값이 들어간다

function displayItems(items){
  const container = document.querySelector('.items');
  container.innerHTML =items.map(item => createHTMLString(item)).join('');
}

function createHTMLString(item){
  return `
  <li class="item">
    <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
    <span class="item__description">${item.gender} ,${item.size}</span>
  </li>
  `;
}
//main

loadItems()
.then(items=>{
  console.log(items);
  displayItems(items);
  setEventListeners(items) 
})
.catch(console.log)