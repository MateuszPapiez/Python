/*
function send_red(){
    let form=new FormData()
    let image_input=document.getElementById("photo_input")
    form.append("file",image_input.files[0])
    axios({
        url:"http://127.0.0.1:5555/image-red",
        data:form,
        headers:{"Content-Type": "multipart/form-data"},
        responseType:'blob',
        method:"POST",
    })

    .then(function(response){
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'file.jpg'); //or any other extension
        document.body.appendChild(link);
        link.click();
        //console.log(response)
    })    
}

function send_crop(){
    let form=new FormData()
    let image_input=document.getElementById("photo_input")
    form.append("file",image_input.files[0])
    axios({
        url:"http://127.0.0.1:5555/image-crop",
        data:form,
        headers:{"Content-Type": "multipart/form-data"},
        responseType:'blob',
        method:"POST",
    })

    .then(function(response){
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'file.jpg'); //or any other extension
        document.body.appendChild(link);
        link.click();
        //console.log(response)
    })    
}
*/