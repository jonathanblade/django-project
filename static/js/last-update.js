function getLastCommit(res) {
  var date = res["commit"]["commit"]["author"]["date"].split("T")[0].split("-");
  var month = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
  };
  var commit = {
    "date": `${date[2].replace(/^0+/, "")} ${month[date[1]]} ${date[0]}`,
    "url": res["commit"]["html_url"]
  }
  return commit;
}

$.ajax({
  type: "GET",
  url: "https://api.github.com/repos/jonathanblade/django-project/branches/master",
  dataType: "json",
  success: function(res) {
    var commit = getLastCommit(res);
    $("#commit-url").prop("href", commit["url"]);
    $("#commit-date").text(commit["date"]);
  }
});