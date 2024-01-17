const likes=document.querySelectorAll('.like')

likes.forEach((like)=>{
  like.addEventListener('click',(e)=>{e.target.classList.toggle('checked');
  });
});