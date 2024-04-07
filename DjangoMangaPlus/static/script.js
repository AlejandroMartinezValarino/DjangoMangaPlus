var wrapper = document.querySelector('.wrapper');

for (var n = 1; n <= 80; n++) {
  var column = document.createElement('div');
  column.className = 'column col-' + n;

  for (var i = 1; i <= 50; i++) {
    var span = document.createElement('span');
    var value = Math.floor(Math.random() * 431) + 256;
    span.textContent = String.fromCharCode(value);
    column.appendChild(span);
  }

  wrapper.appendChild(column);
}
