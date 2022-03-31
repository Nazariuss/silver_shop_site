var inputMin = document.querySelector('#min');
var inputMax = document.querySelector('#max');

var lowerSlider = document.querySelector('#lower'),
    upperSlider = document.querySelector('#upper');
    lowerVal = parseInt(inputMin.value);
    upperVal = parseInt(inputMax.value);

function min_value(ele) {

    if(event.key === 'Enter') {
        if (parseInt(ele.value) <= parseInt(upperSlider.value)) {
            console.log(1)
            lowerSlider.value = ele.value
        } else {
            upperSlider.value = ele.value
            lowerSlider.value = ele.value
            inputMin.value = lowerSlider.value
            inputMax.value = upperSlider.value
        }
    }
}

function max_value(ele) {
    if(event.key === 'Enter') {
        if (parseInt(ele.value) >= parseInt(lowerSlider.value)) {
            upperSlider.value = ele.value
        } else {
            upperSlider.value = ele.value
            lowerSlider.value = ele.value
            inputMin.value = lowerSlider.value
            inputMax.value = upperSlider.value
        }
    }
}

upperSlider.oninput = function() {
   lowerVal = parseInt(lowerSlider.value);
   upperVal = parseInt(upperSlider.value);

   var min = document.getElementById("min")
   var max = document.getElementById("max")
   inputMax.value = upperSlider.value

   if (upperVal < lowerVal + 50) {
      lowerSlider.value = upperVal - 50;
      inputMin.value = lowerSlider.value


      if (lowerVal == lowerSlider.min) {
         upperSlider.value = parseInt(upperSlider.max) + 50;
      }
   }
};


lowerSlider.oninput = function() {
   lowerVal = parseInt(lowerSlider.value);
   upperVal = parseInt(upperSlider.value);

   var min = document.getElementById("min");
   var max = document.getElementById("max");

   inputMin.value = lowerSlider.value

   if (lowerVal > upperVal - 50) {
      upperSlider.value = lowerVal + 50;
      inputMax.value = upperSlider.value


      if (upperVal == upperSlider.max) {
         lowerSlider.value = parseInt(upperSlider.max) - 50;
      }

   }
};

