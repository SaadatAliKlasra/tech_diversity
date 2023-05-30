

// testimonial
$(document).ready(function () {

  $('#team').owlCarousel({
    loop: false,
    margin: 10,
    dots: true,
    nav: false,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 1
      },
      1000: {
        items: 1
      }
    }
  })


  // blog

  $('#blog_slider').owlCarousel({
    loop: false,
    margin: 10,
    dots: true,
    nav: false,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 3
      },
      1000: {
        items: 4,


      }
    }
  })


})


