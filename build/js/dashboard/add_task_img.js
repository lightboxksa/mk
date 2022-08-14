function add_task_img() {
  let img_icon = document.querySelector(".add_img");
  let input_file = document.querySelector("#img_file");

  // console.log(img_icon);

  img_icon.addEventListener("click", function () {
    input_file.click();
  });
}

add_task_img();
