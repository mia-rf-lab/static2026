function renderRandomNum(targetElm, duration) {
  targetElm.each(function (index) {
    let originNum = $(this).data('num');
    $(this).html(originNum);
    $(this).scramble(duration, 10, "numbers");
  });
}

export default renderRandomNum;