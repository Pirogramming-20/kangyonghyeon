//버튼 시간 가져오기
const time = document.getElementById('time');
const btnS = document.getElementById('btnS');
const btnP = document.getElementById('btnP');
const btnR = document.getElementById('btnR');
const rlist = document.getElementById('rlist');

//타이머 표시 부분
let startTime;
let elapsedTime = 0;
let timerInterval;
let millisecondsDigits; 
let formattedSeconds;

//화면에 표시하는 함수
const updateDisplay = () => {
  if (startTime) {
    const currentTime = new Date().getTime();
    elapsedTime = currentTime - startTime;
    time.textContent = formatTime(elapsedTime);
  }
};

// 시간을 포맷팅하는 함수
const formatTime = (milliseconds) => {
  const totalSeconds = Math.floor(milliseconds / 1000);
  const seconds = totalSeconds % 60;
  millisecondsDigits = String(milliseconds % 1000).padStart(3, '0');
  formattedSeconds = String(seconds).padStart(2, '0');
  return `${formattedSeconds}:${millisecondsDigits.substring(0, 2)}`;
};

// 시작 버튼
btnS.addEventListener('click', () => {
  if (!timerInterval) {
    startTime = new Date().getTime() - elapsedTime;
    timerInterval = setInterval(updateDisplay, 100);
  }
});

// 정지 버튼
btnP.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;

  const btn = document.createElement('button');
  btn.setAttribute('id','recordbtn1');
  const div = document.createElement('div');
  div.innerText = `${formattedSeconds}:${millisecondsDigits.substring(0, 2)}`;
  const btn2 = document.createElement('button');
  btn2.classList.add('recordbtn3');

  const li = document.createElement('li');

  li.appendChild(btn);
  li.appendChild(div);
  li.appendChild(btn2);
  rlist.appendChild(li);
});

// 리셋 버튼
btnR.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;
  elapsedTime = 0;
  startTime = new Date().getTime(); // 리셋할 때 현재 시간으로 초기화
  time.textContent = formatTime(elapsedTime);
});

// 함수 실행
updateDisplay();

///기록 버튼 구현

//삭제 구현
rlist.addEventListener('click', (e) => {
  if (e.target.id === 'recordbtn1') {
    const li = e.target.closest('li');
    li.classList.toggle('checked');
  }
});

const removebtn=document.querySelector('.recordbtn2');

removebtn.addEventListener('click',()=>{
  const checked=document.querySelectorAll('.checked');
  checked.forEach(element=>{
    if (element.id !=='recordbtnA'){
      element.remove()
    }
  });
});

const recordHead = document.querySelector('.recordHead');

recordHead.addEventListener('click', (e) => {
  const recordbtnA = document.getElementById('recordbtnA');
  if (e.target.id === 'recordbtnA') {
    recordbtnA.classList.toggle('checked');
    
    // 'checked' 클래스가 적용된 경우
    if (recordbtnA.classList.contains('checked')) {
      const allLi = rlist.querySelectorAll('li:not(.checked)');
      allLi.forEach((li) => {
        li.classList.add('checked');
      });
    } else {
      // 'checked' 클래스가 제거된 경우
      const allLi = rlist.querySelectorAll('li');
      allLi.forEach((li) => {
        li.classList.remove('checked');
      });

      // recordbtnA의 'checked' 클래스도 제거
      recordbtnA.classList.remove('checked');
    }
  }
});

