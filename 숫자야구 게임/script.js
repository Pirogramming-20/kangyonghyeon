let life = 9;
const submitbutton = document.querySelector('.submit-button');

function try_go() {
  const sub = document.querySelectorAll('.input-field');
  const submit = Array.from(sub).map(input => parseInt(input.value, 10));
  //int 같은 함수-> (원하는 값,10(진수))
  const Allinput =submit.every(value=> !isNaN(value));
  //Allinput에 bool값이 들어간다 그때 every모든게 숫자면 true 그렇지 않으면 false

  if (!Allinput){
    console.log('다채워');
    clearinput();
    return;
    //Allinput 이 true면 실행하지않고 false실행한다
  }
  console.log(`Life: ${life}`);
  if (life === 0) {
    submitbutton.disabled = true;
    //life=0이면 submition 버튼을 작동시키지않는다
  }
  clearinput();
  //값이 들어올떄 마다 입력 필드를 지운다
}

submitbutton.addEventListener('click', try_go);
//버튼 눌리면 trygo를 실해한다 subbbmit 버튼을 만들었고

// 정답 생성 함수
function answercreate(count, min, max) {
  if (count > (max - min + 1) || max < min) {
    return null;
  }
  const answ_num = [];
  while (answ_num.length < count) {
    const randomnum = Math.floor(Math.random() * (max - min + 1)) + min;
    if (!answ_num.includes(randomnum)) {
      answ_num.push(randomnum);
    }
  }
  return answ_num;
}
//python처럼 랜덤으로 숫자를 생성한다
const answer = answercreate(3, 0, 9);
//함수를 변수에 대입한다-> 그래서 answer를 만든다

//check-numbers는 HTML에서 정의한 버튼이다
// input을 array로 가져오기
function check_numbers() {
  const sub = document.querySelectorAll('.input-field');
  const submit = Array.from(sub).map(input => parseInt(input.value, 10));
  //인풋 채워지지 않으면 게임 안되게 
  const Allinput =submit.every(value=> !isNaN(value));

  if (!Allinput){
    console.log('다채워')
    return;
  }
//똑같이 submit을 정의한다 근데 굳이 submit을 두번 정의할필요가 있을까..?
  handleGame(submit);
  console.log('Submit:', submit);
  console.log('Answer:', answer);
}  
  // 비교하기
function handleGame(submit) {
  let strike = 0;
  let ball = 0;

  for (let i = 0; i < answer.length; i++) {
    if (answer[i] === submit[i]) {
      strike++;
    } else if (answer.includes(submit[i])) {
      ball++;
    }
  }
//자리가 같으면 스트라이크 include하면 ball준다. 
  if (strike === 3) {
    const success = document.getElementById('game-result-img');
    success.src = './success.png';
  } else if (life === 1 && strike !== 3) {
    const fail = document.getElementById('game-result-img');
    fail.src = './fail.png';
  }

  if (strike === 0 && ball === 0) {
    console.log('out');
    const resultHTML = createHTMLString(submit, { strike, ball });
    console.log(resultHTML);
    displayItems(resultHTML);
    clearinput();
  } else {
    console.log(`Strike: ${strike}, Ball: ${ball}`);
    const resultHTML = createHTMLString(submit, { strike, ball });
    console.log(resultHTML);
    displayItems(resultHTML);
  }
//이거는
  life--;
  console.log(`${life}`);
  if (life === 0) {
    submitbutton.disabled = true;
  }
}
// input 비우는 함수
function clearinput() {
  const sub = document.querySelectorAll('.input-field');
  sub.forEach(input => (input.value = ''));
}

submitbutton.addEventListener('click', check_numbers);

//결과 값을 화면에 출력

//이부분 함수 정의
function createHTMLString(submit, { strike, ball }) {
  const submitnum = submit.join(' ');


  if (strike === 0 && ball === 0) {
    return `
      <div class="check-result">
        <div class="left">${submitnum}</div>
        :
        <div class="right">
          <div class="out num-result">O</div>
        </div>
      </div>
    `;
  } else {
    return `
      <div class="check-result">
        <div class="left">${submitnum}</div>
        :
        <div class="right">
          ${strike} <div class="strike num-result">S</div>
          ${ball} <div class="ball num-result">B</div>
        </div>
      </div>
    `;
  }
}


function displayItems(htmlString) {
  const container = document.querySelector('.result-display');
  if (!container) {
    console.error("Error: .result-display element not found");
    return;
  }

  const resultElement = document.createElement('div');
  resultElement.innerHTML = htmlString;
  container.appendChild(resultElement);
}

