function copy_text(e){
    e.innerText = ""
    navigator.clipboard.writeText(e.parentNode.innerText).then(()=>{
        e.innerText = "Copied!"
        setTimeout(()=>{
            e.innerText = "Copy"
        },2000)
    });
}

