function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getReceptionsValue() {
  var uiReceptions = document.getElementsByName("uiReceptions");
  for(var i in uiReceptions) {
    if(uiReceptions[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBedroomsValue() {
  var uiBedrooms = document.getElementsByName("uiBedrooms");
  for(var i in uiBedrooms) {
    if(uiBedrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bedrooms = getBedroomsValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");
  var house_type = document.getElementById("uiTypes");
  var receptions = getReceptionsValue();

  var url = "/api/predict_home_price";

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bedrooms: bedrooms,
      bathrooms: bathrooms,
      location: location.value,
      house_type: house_type.value,
      receptions: receptions,
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>&pound;" + data.estimated_price.toString();
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "/api/get_location_names";
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

function onPageLoad2() {
  console.log( "document loaded" );
  var url = "/api/get_house_types_names";
  $.get(url,function(data, status) {
      console.log("got response for get_house_type_names request");
      if(data) {
          var house_type = data.house_types;
          var uiTypes = document.getElementById("uiTypes");
          $('#uiTypes').empty();
          for(var i in house_type) {
              var opt = new Option(house_type[i]);
              $('#uiTypes').append(opt);
          }
      }
  });
}

function init(){
  onPageLoad();
  onPageLoad2();
}

window.onload = init();