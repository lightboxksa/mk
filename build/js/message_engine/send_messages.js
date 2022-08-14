function send_messages() {
  let received_numbers = document.querySelectorAll(".received_number");
  let header_number = document.querySelector(".header_this_number");
  let full_background = document.querySelector(".full_element_back");
  let this_message = document.querySelector(".this_message");
  let this_time = document.querySelector(".this_time");
  let icon_send = document.querySelector("#icon_send");
  let input_this_message = document.querySelector(
    "#input_this_message_content"
  );
  let message_content = document.querySelector("#message_cont");

  const sleep = (milliseconds) => {
    return new Promise((resolve) => setTimeout(resolve, milliseconds));
  };

  const doSomething = async () => {
    for (let index = 0; index < received_numbers.length; index++) {
      header_number.textContent =
        received_numbers[index].getAttribute("number");

      this_message.classList.add("none");
      
      this_time.textContent = "";
      await sleep(50);
      input_this_message.value = message_content.textContent;

      await sleep(3000);
      icon_send.style.color = "#1c9183";
      await sleep(500);
      received_numbers[index].classList.add("phone-activate");
      this_message.classList.remove("none");
      input_this_message.value = "";
      icon_send.style.color = "#40475c";

      let today = new Date();
      if (today.getMinutes().length == 1){
        this_time.textContent = today.getHours() + ":" + `0${today.getMinutes()}`;
      } else {
        this_time.textContent = today.getHours() + ":" + today.getMinutes();
      }
      await sleep(2000);
    }
    await sleep(500);
    full_background.classList.remove("none");
  };

  doSomething();
}

send_messages();
