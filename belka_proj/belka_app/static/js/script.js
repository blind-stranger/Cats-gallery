import PhotoSwipeLightbox from './photoswipe-lightbox.esm.js';

const GALLERY_ID = "gallery"

let images = []
let count = 0
let gallery = document.getElementById(GALLERY_ID)

let maximum = 0
gallery.childNodes.forEach(item => {
  if (maximum < item.childElementCount) maximum = item.childElementCount
})

for (let i = 0; i < maximum; i++) {
  for (let j = 0; j < 3; j++) {
    let item = gallery.children[j].children[i]
    if (item) {
      images.push({
        id: count,
        src: item.href,
        width: item.dataset.pswpWidth,
        height: item.dataset.pswpHeight
      })
      count++
    }
    
  }
}

const lightbox = new PhotoSwipeLightbox({
  dataSource: images,
  pswpModule: () => import('./photoswipe.esm.js'),
  wheelToZoom: true,
  padding: { top: 20, bottom: 20, left: 100, right: 100 },
  secondaryZoomLevel: "fit",
  maxZoomLevel: 1,
  wheelToZoom: true
});
lightbox.init();

lightbox.addFilter('thumbEl', (thumbEl, data, index) => {
  const el = gallery.querySelector('[data-id="' + data.id + '"] img');
  if (el) {
    return el;
  }
  return thumbEl;
});
lightbox.addFilter('placeholderSrc', (placeholderSrc, slide) => {
  const el = gallery.querySelector('[data-id="' + slide.data.id + '"] img');
  if (el) {
    return el.src;
  }
  return placeholderSrc;
});


window.pswpLightbox = lightbox;