

function fetch_messages(){
    axios.get("http://127.0.0.1:5555/get-messages")
    .then(function (response){
        console.log(response)
        let messages=response.data
        let messages_div= document.getElementById("message")
        messages_div.innerHTML=""
        for (let i=0; i<messages.length ;i++){
            let msg_div = document.createElement("div")
            msg_div.className="msg";
            msg_div.innerHTML = messages[i].login+"<br>" + messages[i].content
            messages_div.appendChild(msg_div);
        } 
    }) 

}
fetch_messages()
function send_message (){
    let login=document.getElementById("login").value
    let content=document.getElementById("content").value
    let req={
        login:login,
        content:content
    }
    axios.post("http://127.0.0.1:5555/send-message",req)
    .then (function(response){
        console.log(response)
        fetch_messages()
    })

    
}
setInterval (fetch_messages,1000)