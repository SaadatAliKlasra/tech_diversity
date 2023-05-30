// Header Scroll Fixed animation

jQuery(window).scroll(function() {
  if (jQuery(this).scrollTop() > 50) {
    jQuery("#header").addClass('affix');
  } else {
    jQuery("#header").removeClass('affix');
  }
});




