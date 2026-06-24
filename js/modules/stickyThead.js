function stickyThead() {
  const thead = document.querySelector('.sticky-thead');
  const tbody = document.querySelector('.sticky-tbody');

  const theadInitialBottom = thead.offsetHeight + 72; // header height = 72px

  const tbodyRect = tbody.getBoundingClientRect();
  const tbodyTop = tbodyRect.top;
  const tbodyBottom = tbodyRect.bottom;

  const isSticky = tbodyTop <= 72;

  if (isSticky) {
    thead.classList.add('is-sticky');

    // 計算 tbody 底部與 thead 初始底部之間的差距
    const translateY = tbodyBottom - theadInitialBottom;

    // 只有當 tbody 底部即將超過 thead 底部時，才開始向上移動
    if (translateY < 0) {
      thead.style.transform = `translateY(${translateY}px)`;
    } else {
      thead.style = ''; // 保持在頂部
    }

  } else {
    thead.classList.remove("is-sticky");
    thead.style = ''; // 保持在頂部
  }
}

document.addEventListener('DOMContentLoaded', () => {
  stickyThead();
});

window.addEventListener('scroll', () => {
  stickyThead();
});

window.addEventListener('resize', () => {
  stickyThead();
});