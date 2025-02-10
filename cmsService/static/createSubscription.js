function callbackFunction(event) {
    event.preventDefault();
    const myFormData = new FormData(event.target);
    console.log(myFormData)

    const formDataObj = {};
    myFormData.forEach((value, key) => (formDataObj[key] = value));
   
    fetchOptions.body = JSON.stringify(formDataObj);

    fetch(url_sendmessage, fetchOptions)
    .then((response)=>{
        return response.json();

    })

    document.getElementById("createSubscription").reset();
}


const url_sendmessage = "/api/v1/editor/create"
var fetchOptions = {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    }
}

const form = document.getElementById("createSubscription");
form.addEventListener('submit', callbackFunction);
