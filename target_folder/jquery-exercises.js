$(function() {
    $("#static-numbers-button").click(showNumbers1);
    $("#dynamic-numbers-button").click(showNumbers2);
    $("#slow-numbers-button").click(showNumbers3);
});

function makeList(numberObject) {
  return("<ul>\n" +
         "  <li>" + numberObject.num1 + "</li>\n" +
         "  <li>" + numberObject.num2 + "</li>\n" +
         "  <li>" + numberObject.num3 + "</li>\n" +
         "</ul>");
}

function makeList1(numberObject) {
  var numberList = makeList(numberObject);
  $("#static-numbers-result").html(numberList);
}

function showNumbers1() {
  $.ajax({
    url: "numbers.json",
    success: makeList1,
    dataType: "json"
  });
}

function makeList2(numberObject) {
  var numberList = makeList(numberObject);
  $("#dynamic-numbers-result").html(numberList);
}

function showNumbers2() {
  $.ajax({
    url: "numbers.jsp",
    success: makeList2,
    dataType: "json"
  });
}

function makeList3(numberObject) {
  var numberList = makeList(numberObject);
  $("#slow-numbers-result").html(numberList);
}

function showNumbers3() {
  var workingRegion = "#working";
  var resultRegion = "#slow-numbers-result";
  $(resultRegion).html(""); // Erase any previous results
  $(workingRegion).show();
  $.ajax({
    url: "slow-numbers.jsp",
    success: makeList3,
    complete: function() { $(workingRegion).hide(); },
    dataType: "json"
  });
}