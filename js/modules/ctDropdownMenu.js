function replaceStr(sourceStr, relaceTarget){
  let str = sourceStr.text(); // Get string from source element
  relaceTarget.text(str); // Then sync it to target element
}


function ctDropdownMenu(target, activedItm, strContainer){

  replaceStr(activedItm, strContainer); // Run function once when page loaded

  // When RWD dropdown menu opened and click any <a> elements...
  target.find('a').click(function(){

    // 1. Switch active status between <a>
    $(this).addClass('active').parent().siblings('li').find('a').removeClass('active');

    // 2. Remove the class ".open" in parent element
    target.removeClass('open');

    // 3. Run each time user click a item
    replaceStr($(this), strContainer);

    // 4. Scroll to the best position on small screen
    // if( mqIpadPortrait.matches ) { // If CSS mediaqueries is equal => (max-width: 767px)
    //   let targetPos = target.offset().top; // Get target position in the page
    //   let headerHeight = $('header.site-header').outerHeight(); // Get the height of header (Site Nav)
    //   let scrollToPos = targetPos - headerHeight - 10; // Calculate the best position to scroll

    //   $('html,body').delay(400).animate({ // Delay 400ms for css animation of closing dropdown menu
    //     scrollTop: scrollToPos
    //   }, 500); // Duration: 500ms
    // }
  });

  // When RWD dropdown menu wasn't open and click <span> elements
  strContainer.click(function(){
    target.toggleClass('open'); // Open the RWD dropdown menu
  });

  // Click outside of RWD dropdown menu(anywhere) to close menu
  const $menu = target;
  $(document).mouseup(function (e) {
    // if clicking target isn't the container or not a descendant of the container
    if (!$menu.is(e.target) && $menu.has(e.target).length === 0 ) {
      $menu.removeClass('open');
    }
  });
}


if( $('.js-dropdown').length ) {
  $('.js-dropdown').each(function(){
    let target = $(this);
    let activedItm = $(this).find('a.active');
    let strContainer = $(this).children('span');

    ctDropdownMenu(target, activedItm, strContainer);
  });
}


$(window).resize(function(){
  // Close Custom Dropdown Menu
  if( $('.js-dropdown').length ) {
    $('.js-dropdown').removeClass('open');
  }
});