const button = document.querySelector('#hello');

button?.addEventListener('click', () => {
  document.querySelector('#message').textContent = 'You made it happen. Keep creating! ✨';
  console.log('A little magic, made by you.');
});

console.log('Ready when you are. ✨');