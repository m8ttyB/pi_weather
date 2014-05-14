$(document).ready(function() {
  $.ajax({
      url: "http://10.0.1.137:4444/weather/api/v1.0/temperature",
      contentType: "application/json",
      dataType: "json",
      success: function(data){ 
          console.log(data);
          $('#fahrenheit').append(JSON.stringify(data.weather_data));
          $('#fahrenheit').append(String(data.weather_data));
      },
      error: function (data, jqXHR, textStatus, errorThrown) {
          $("#error").append("<h3>Error message</h3>jqXHR: " + jqXHR.status + "\ntextStatus: " + textStatus + "\nerrorThrown: " + errorThrown);
          $("#error").append("<p>data: " + JSON.stringify(data) + "</p>");
      }
  });

});
