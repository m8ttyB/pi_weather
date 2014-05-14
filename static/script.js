$(document).ready(function() {
  $.ajax({
      url: "http://10.0.1.137:4444/weather/api/v1.0/temperature",
      contentType: "application/json",
      dataType: "json",
      success: function(response){ 
          $('#fahrenheit').append(response.weather_data[0].fahrenheit[0]);
      },
      error: function (data, jqXHR, textStatus, errorThrown) {
          $("#error").append("<h3>Error message</h3>jqXHR: " + jqXHR.status + "\ntextStatus: " + textStatus + "\nerrorThrown: " + errorThrown);
          $("#error").append("<p>data: " + JSON.stringify(data) + "</p>");
      }
  });

});
