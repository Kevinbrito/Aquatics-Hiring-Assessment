let tabContainer = document.getElementById("assessHeader")

let tabs = tabContainer.getElementsByClassName("nav-link")

function deactivate() {
    let allTabs = tabContainer.getElementsByClassName("active");
    Array.from(allTabs).forEach((element) => {
        element.className = "nav-link text-warning";
    });
}

for (let index = 0; index < tabs.length; index++) {
    tabs[index].addEventListener("click", function () {
        deactivate()
        this.className += " active";
    })
}

$(document).ready(function(){

  // jQuery methods go here...

  // onLoad handling...
    $("#secOneBody").hide();

  // eventHandling functions...
    $("#secOneTab").click(function () {
        $("#registerBody").hide();
        $("#secOneBody").show();
    })

    $("#registerTab").click(function () {
        $("#secOneBody").hide();
        $("#registerBody").show();
    })
});
