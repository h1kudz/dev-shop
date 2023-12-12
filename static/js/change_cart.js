
let col = document.getElementById('id_quantity');
let plus = document.getElementById('plus');
let minus = document.getElementById('minus');

plus.onclick = function() {
col.value = parseInt(col.value) + 1;
}

minus.onclick = function() {
col.value = parseInt(col.value) - 1;
}

