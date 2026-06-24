// [Custom function] Overcoming CSS Not Calculating Auto-Height For Transitions
function reCalcHeight(elm) {
  if ( !elm ) {
    var calcTargets = document.getElementsByClassName('js-calc-height');
  } else {
    var calcTargets = document.getElementsByClassName(elm);
  }

  for (var target of calcTargets) {
    if (target.style.getPropertyValue("--calc-height") == false) {

      let value = target.offsetHeight + "px";
      target.style.setProperty("--calc-height", value);
      target.classList.add("calc-height-loaded");

    } else {

      target.style.setProperty("--calc-height", "");
      target.classList.remove("calc-height-loaded");

      let value = target.offsetHeight + "px";
      target.style.setProperty("--calc-height", value);
      target.classList.add("calc-height-loaded");

    }
  }
}

reCalcHeight(); // Fire once when page loaded

$(window).resize(function(){
  reCalcHeight(); // Fire when page scrolled
});