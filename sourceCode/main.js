const input = document.querySelector("#keywords");
const perik = document.querySelector("#periksa");
const fP = document.querySelector("#formPeriksa");
fetch(url, {
  method: "GET",
})
  .then((res) => res.json())
  .then((data) => {
    kalimat = data.kalimat;
  });
let currentFocus;

perik.addEventListener("click", (e) => {
  fP.submit();
});

input.addEventListener("focus", (e) => {
  let a,
    b,
    i,
    val = input.value;
  closeAllLists();
  if (!val) {
    return false;
  }
  currentFocus = -1;

  a = document.createElement("div");
  a.setAttribute("id", a.id + "autocomplete-list");
  a.setAttribute("class", "autocomplete-items");
  input.parentNode.appendChild(a);

  for (i = 0; i < kalimat.length; i++) {
    if (kalimat[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
      b = document.createElement("div");
      b.innerHTML = `<strong>${kalimat[i].substr(0, val.length)}</storng>`;
      b.innerHTML += kalimat[i].substr(val.length);
      b.innerHTML += `<input type='hidden' value='${kalimat[i]}'>`;
      b.addEventListener("click", (e) => {
        input.value = b.getElementsByTagName("input")[0].value;
        closeAllLists();
      });
      a.appendChild(b);
    }
  }
});

input.addEventListener("input", (e) => {
  let a,
    b,
    i,
    val = input.value;
  closeAllLists();
  if (!val) {
    return false;
  }
  currentFocus = -1;

  a = document.createElement("div");
  a.setAttribute("id", a.id + "autocomplete-list");
  a.setAttribute("class", "autocomplete-items");
  input.parentNode.appendChild(a);

  for (i = 0; i < kalimat.length; i++) {
    if (kalimat[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
      b = document.createElement("div");
      b.innerHTML = `<strong>${kalimat[i].substr(0, val.length)}</storng>`;
      b.innerHTML += kalimat[i].substr(val.length);
      b.innerHTML += `<input type='hidden' value='${kalimat[i]}'>`;
      b.addEventListener("click", (e) => {
        input.value = b.getElementsByTagName("input")[0].value;
        closeAllLists();
      });
      a.appendChild(b);
    }
  }
});

// input.addEventListener("focusout", (e) => {
//   closeAllLists();
// });

input.addEventListener("keydown", (e) => {
  var x = document.getElementById(input.id + "autocomplete-list");
  if (x) x = x.getElementsByTagName("div");
  if (e.keyCode == 40) {
    currentFocus++;
    addActive(x);
  } else if (e.keyCode == 38) {
    currentFocus--;
    addActive(x);
  } else if (e.keyCode == 13) {
    e.preventDefault();
    if (currentFocus > -1) {
      if (x) x[currentFocus].click();
    }
  }
});
function addActive(x) {
  if (!x) return false;
  removeActive(x);
  if (currentFocus >= x.length) currentFocus = 0;
  if (currentFocus < 0) currentFocus = x.length - 1;
  x[currentFocus].classList.add("autocomplete-active");
}

function removeActive(x) {
  for (var i = 0; i < x.length; i++) {
    x[i].classList.remove("autocomplete-active");
  }
}

function closeAllLists(elmnt) {
  var x = document.getElementsByClassName("autocomplete-items");
  for (var i = 0; i < x.length; i++) {
    if (elmnt != x[i] && elmnt != input) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}

document.addEventListener("click", function (e) {
  closeAllLists(e.target);
});

