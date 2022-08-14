function add_tasks_city_filter() {
  // console.log("add_tasks_city_filter");
  let country = document.getElementById("country");
  let cites = document.querySelectorAll("#city option.city_option");

  setInterval(function () {
    for (let index = 0; index < cites.length; index++) {
      if (cites[index].getAttribute("country") != country.value) {
        cites[index].classList.add("none");
      } else {
        cites[index].classList.remove("none");
      }
    }
  }, 500);
}
add_tasks_city_filter();
